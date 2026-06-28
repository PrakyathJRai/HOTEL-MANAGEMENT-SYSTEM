from django.http import HttpResponseForbidden
from functools import wraps


def doctor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print("========== DEBUG ==========")
        print("Username:", request.user.username)
        print("Email:", request.user.email)
        print("Role:", request.user.role)
        print("===========================")

        if not request.user.is_authenticated:
            return HttpResponseForbidden("Please login.")

        if request.user.role != "doctor":
            return HttpResponseForbidden("Only doctors can access this page.")

        return view_func(request, *args, **kwargs)

    return wrapper


def patient_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        print("========== PATIENT DEBUG ==========")
        print("Authenticated:", request.user.is_authenticated)
        print("Username:", request.user.username)
        print("Email:", request.user.email)
        print("Role:", request.user.role)
        print("===================================")

        if not request.user.is_authenticated:
            return HttpResponseForbidden("Please login.")

        if request.user.role != "patient":
            return HttpResponseForbidden("Only patients can access this page.")

        return view_func(request, *args, **kwargs)

    return wrapper