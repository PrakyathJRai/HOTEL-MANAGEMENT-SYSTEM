import json
import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "prakyathjrai963@gmail.com"
SENDER_PASSWORD = "ubrqbepbfpuvbnfz"

def send_email(event, context):
    try:
        body = json.loads(event["body"])

        email = body["email"]
        email_type = body["type"]

        print("Sending email to:", email)
        print("Email type:", email_type)

        if email_type == "SIGNUP_WELCOME":
            subject = "Welcome to Hospital Management System"
            message = "Welcome! Your account has been created successfully."

        elif email_type == "BOOKING_CONFIRMATION":
            subject = "Appointment Confirmed"
            message = "Your appointment has been booked successfully."

        else:
            subject = "Notification"
            message = "Hospital Notification"

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
        server.quit()

        print(" Email sent successfully!")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent"})
        }

    except Exception as e:
        print(" EMAIL ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }