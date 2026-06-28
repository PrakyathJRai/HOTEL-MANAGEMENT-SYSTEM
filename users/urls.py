from django.urls import path
from . import views
from appointments import views as appointment_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("doctor/", views.doctor_dashboard, name="doctor_dashboard"),

    path(
        "patient/",
        appointment_views.patient_dashboard,
        name="patient_dashboard",
    ),

    # Google Calendar OAuth
    
]