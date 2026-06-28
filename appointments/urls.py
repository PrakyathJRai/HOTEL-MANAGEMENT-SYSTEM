from django.urls import path
from . import views

urlpatterns = [
    path(
        "availability/",
        views.add_availability,
        name="add_availability"
    ),

    path(
        "patient-dashboard/",
        views.patient_dashboard,
        name="patient_dashboard"
    ),

    path(
        "book/<int:slot_id>/",
        views.book_slot,
        name="book_slot"
    ),

    path(
        "my-appointments/",
        views.my_appointments,
        name="my_appointments"
    ),
]