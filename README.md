# 🏥 Hospital Management System

A Hospital Management System built using **Django** that enables doctors to manage their availability and patients to book appointments. The system also integrates **Google Calendar** and a **Serverless Email Notification Service**.

---

## Features

- User Registration and Login
- Role-based Authentication (Doctor & Patient)
- Doctor Dashboard
- Patient Dashboard
- Doctor Availability Management
- Appointment Booking
- Prevents Double Booking
- Google Calendar Integration
- Email Notifications using Serverless Framework
- Responsive UI using Django Templates

---

## Tech Stack

### Backend
- Python
- Django
- PostgreSQL

### Authentication
- Django Authentication
- Google OAuth (Google Calendar API)

### Email Service
- Node.js
- Serverless Framework

### Frontend
- HTML
- CSS
- Bootstrap
- Django Templates

---

## Project Structure

```
Hospital-Management-System/
│
├── appointments/
├── users/
├── templates/
├── static/
├── email-service/
├── hms/
├── manage.py
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/HOTEL-MANAGEMENT-SYSTEM.git

cd HOTEL-MANAGEMENT-SYSTEM
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

### Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## Email Service

Go inside

```bash
cd email-service
```

Install packages

```bash
npm install
```

Run locally

```bash
npx serverless offline
```

---

## Google Calendar Setup

1. Create OAuth credentials in Google Cloud Console.
2. Enable Google Calendar API.
3. Download OAuth Client credentials.
4. Place `credentials.json` in the project root.
5. Add the following Redirect URI:

```
http://127.0.0.1:8000/accounts/google/login/callback/
```

> **Important:** Do **not** commit `credentials.json` or `.env` files to GitHub.

---

## Workflow

Doctor

- Login
- Add availability
- Manage appointments
- Sync appointments with Google Calendar

Patient

- Login
- View available slots
- Book appointment
- Receive booking confirmation email

---

## Security

The following files are excluded from GitHub:

```
credentials.json
.env
.env.local
venv/
__pycache__/
```

---

## Future Improvements

- Video Consultation
- Online Payments
- Medical Records
- Admin Analytics Dashboard
- SMS Notifications
- Prescription Management

---

## Author

**Prakyath J Rai**

GitHub:
https://github.com/PrakyathJRai

---

## License

This project was developed as part of the Python Serverless Backend Track Assignment.