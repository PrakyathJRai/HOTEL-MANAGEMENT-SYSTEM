import requests

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import transaction
from django.http import HttpResponse

from users.decorators import doctor_required, patient_required

from .forms import AvailabilityForm
from .models import Availability, Booking


# ---------------------------
# Doctor Dashboard
# ---------------------------
@login_required
@doctor_required
def add_availability(request):

    print("========== DOCTOR DEBUG ==========")
    print("Username:", request.user.username)
    print("Email:", request.user.email)
    print("Role:", request.user.role)
    print("==================================")

    if request.method == "POST":
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            availability = form.save(commit=False)
            availability.doctor = request.user
            availability.save()

            return redirect("add_availability")

    else:
        form = AvailabilityForm()

    slots = Availability.objects.filter(
        doctor=request.user
    ).order_by("date", "start_time")

    return render(
        request,
        "add_availability.html",
        {
            "form": form,
            "slots": slots,
        },
    )


# ---------------------------
# Patient Dashboard
# ---------------------------
@login_required
@patient_required
def patient_dashboard(request):

    today = timezone.localdate()

    slots = Availability.objects.filter(
        is_booked=False,
        date__gte=today
    ).order_by("date", "start_time")

    print("\n========== AVAILABLE SLOTS ==========")
    for slot in slots:
        print(
            f"ID={slot.id}, Date={slot.date}, "
            f"Booked={slot.is_booked}, Doctor={slot.doctor.username}"
        )
    print("=====================================\n")

    return render(
        request,
        "patient_dashboard.html",
        {
            "slots": slots,
        },
    )


# ---------------------------
# Book Appointment
# ---------------------------
@login_required
@patient_required
def book_slot(request, slot_id):

    with transaction.atomic():

        slot = Availability.objects.select_for_update().filter(
            id=slot_id
        ).first()

        if slot is None:
            return HttpResponse("Slot not found.")

        if slot.is_booked:
            return HttpResponse("Sorry! This slot has already been booked.")

        booking = Booking.objects.create(
            doctor=slot.doctor,
            patient=request.user,
            availability=slot
        )

        slot.is_booked = True
        slot.save()

    # -------------------------
    # Send Booking Confirmation Email
    # -------------------------
    try:
        response = requests.post(
            "http://localhost:3000/dev/send-email",
            json={
                "type": "BOOKING_CONFIRMATION",
                "email": request.user.email,
            },
            timeout=5,
        )

        print("========== BOOKING EMAIL ==========")
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        print("===================================")

    except Exception as e:
        print("BOOKING EMAIL ERROR:", e)

    return redirect("my_appointments")


# ---------------------------
# My Appointments
# ---------------------------
@login_required
@patient_required
def my_appointments(request):

    bookings = Booking.objects.filter(
        patient=request.user
    ).select_related(
        "doctor",
        "availability"
    ).order_by("-booked_at")

    return render(
        request,
        "my_appointments.html",
        {
            "bookings": bookings,
        },
    )