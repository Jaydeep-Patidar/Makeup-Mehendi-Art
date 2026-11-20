# Makeup & Mehendi Art

A Django-powered website for a makeup and mehendi artist. The application brings service discovery, portfolio browsing, appointment booking, customer enquiries, and content management together in one place.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Django-5.1.3-092E20?logo=django&logoColor=white" alt="Django 5.1.3">
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-E34F26?logo=html5&logoColor=white" alt="HTML CSS JavaScript">
</p>

## Overview

The project provides a web presence for a makeup and mehendi business, with account access and Django admin tools for managing business content and enquiries.

## Features

- **Service catalogue** — display services, descriptions, and images.
- **Portfolio gallery** — organize creative work by Makeup, Mehendi, Bridal, and Party categories.
- **Appointment booking** — collect customer details, preferred service, date, and time.
- **Booking email notifications** — send booking confirmation and administrator notifications when SMTP is configured.
- **Contact enquiries** — save customer messages and send email notifications.
- **Customer accounts** — registration, login, and logout.
- **Testimonials** — manage and display customer feedback.
- **Django admin** — manage services, portfolio entries, testimonials, bookings, and contact submissions.
- **Media uploads** — store images for services and portfolio content.

## Application screenshots

All previews below were captured from the supplied screen recording of the running project.

<p align="center">
  <img src="screenshots/main-pages.webp" alt="Home, services, portfolio and contact page previews" width="90%">
</p>

<p align="center">
  <img src="screenshots/additional-pages.webp" alt="Login, registration, booking, about and testimonials page previews" width="90%">
</p>

| Preview | Included pages |
| --- | --- |
| Main pages | Home, Services, Portfolio, Contact |
| Additional pages | Login, Registration, Booking, About, Testimonials |

## Tech stack

| Area | Technology |
| --- | --- |
| Language | Python |
| Backend | Django 5.1.3 |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Database | SQLite (default local setup) |
| Image uploads | Pillow |
| Email | Django email backend / SMTP |

## Project structure

```text
Makeup-Mehendi-Art/
├── MyDemo/                 # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/               # Registration, login, logout
│   ├── accounts_url.py
│   ├── forms.py
│   └── views.py
├── home/                   # Website pages and business features
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── admin.py
├── public/                 # Project static assets
├── media/                  # User-uploaded media (local only)
├── .env.example            # Environment variable reference
├── .gitignore
├── manage.py
└── requirements.txt
```

## Getting started

### Requirements

- Python 3.10 or newer
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Jaydeep-Patidar/Makeup-Mehendi-Art.git
cd Makeup-Mehendi-Art
```

### 2. Create and activate a virtual environment

**Windows (PowerShell / Command Prompt):**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Use `.env.example` as a reference and set the variables in your shell or hosting provider. The project does not automatically load a `.env` file.

For a local development run, the defaults are configured for localhost and console email output. Set a private `SECRET_KEY` and `DEBUG=False` before deploying.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Main routes

| Route | Purpose |
| --- | --- |
| `/` | Landing page |
| `/home/` | Main home page |
| `/portfolio/` | Portfolio gallery |
| `/services/` | Services |
| `/booking/` | Appointment booking |
| `/booking/data/` | Booking calendar data |
| `/contact/` | Contact form |
| `/accounts/login/` | Account login (see accounts URL configuration) |
| `/admin/` | Django administration |

Some website pages are protected by login. Create an account through the application's registration page before accessing protected pages.

## Email configuration

The default development email backend writes messages to the terminal. To enable SMTP, configure the following environment variables:

- `EMAIL_BACKEND` — for example, `django.core.mail.backends.smtp.EmailBackend`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_USE_TLS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `DEFAULT_FROM_EMAIL`
- `ADMIN_EMAIL`

Never commit real email credentials or secret keys.

## Development notes

- Uploaded files are stored under `media/` in local development. Configure persistent media storage for deployment.
- SQLite is intended for the included local setup. Choose and configure a production database and backups before deployment.
- Run `python manage.py check` after changing Django configuration.
- Add automated tests for booking, authentication, and contact workflows before production release.

## Future improvements

- Add automated tests for core workflows.
- Add pagination and search to the portfolio and admin listings.
- Add booking validation and availability checks.
- Configure production-grade static and media storage.
- Add a deployment guide and CI checks.

## Author

**Jaydeep Patidar**

- GitHub: [@Jaydeep-Patidar](https://github.com/Jaydeep-Patidar)

---

If you find this project useful, consider giving the repository a star.
