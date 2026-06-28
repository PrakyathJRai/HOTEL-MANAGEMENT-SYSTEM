import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

from google_auth_oauthlib.flow import Flow

from .forms import SignUpForm


SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


# --------------------------------
# Signup
# --------------------------------
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Send Welcome Email
            try:
                response = requests.post(
                    "http://localhost:3000/dev/send-email",
                    json={
                        "type": "SIGNUP_WELCOME",
                        "email": user.email,
                    },
                    timeout=5,
                )

                print("========== EMAIL SERVICE ==========")
                print("STATUS :", response.status_code)
                print("RESPONSE :", response.text)
                print("===================================")

            except Exception as e:
                print("EMAIL SERVICE ERROR:", e)

            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend"
            )

            if user.role == "doctor":
                return redirect("doctor_dashboard")

            return redirect("patient_dashboard")

        else:
            print(form.errors)

    else:
        form = SignUpForm()

    return render(
        request,
        "signup.html",
        {
            "form": form
        }
    )


# --------------------------------
# Login
# --------------------------------
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user,
                backend="django.contrib.auth.backends.ModelBackend"
            )

            if user.role == "doctor":
                return redirect("doctor_dashboard")

            return redirect("patient_dashboard")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(request, "login.html")


# --------------------------------
# Logout
# --------------------------------
def logout_view(request):
    logout(request)
    return redirect("login")


# --------------------------------
# Doctor Dashboard
# --------------------------------
def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html")


# --------------------------------
# Google Calendar OAuth
# --------------------------------
def google_connect(request):

    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, "credentials.json"),
        scopes=SCOPES,
    )

    flow.redirect_uri = "http://127.0.0.1:8000/google/callback/"

    print("REDIRECT URI:", flow.redirect_uri)

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent",
    )

    print("AUTH URL:", authorization_url)

    request.session["state"] = state

    return redirect(authorization_url)


def google_callback(request):

    flow = Flow.from_client_secrets_file(
        os.path.join(settings.BASE_DIR, "credentials.json"),
        scopes=SCOPES,
        state=request.session["state"],
    )

    flow.redirect_uri = request.build_absolute_uri("/google/callback/")

    flow.fetch_token(
        authorization_response=request.build_absolute_uri()
    )

    credentials = flow.credentials

    request.user.google_access_token = credentials.token
    request.user.google_refresh_token = credentials.refresh_token
    request.user.google_token_expiry = credentials.expiry

    request.user.save()

    return redirect("doctor_dashboard")