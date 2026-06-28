from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


def get_calendar_service(user):
    """
    Create a Google Calendar service using
    the user's stored OAuth tokens.
    """

    creds = Credentials(
        token=user.google_access_token,
        refresh_token=user.google_refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        scopes=SCOPES,
    )

    return build("calendar", "v3", credentials=creds)