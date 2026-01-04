# MyDemo - Makeup and Mehndi Service Website

A Django-based web application for a makeup and mehndi service business, allowing users to view services, portfolio, book appointments, and contact the business.

## Features

- **Home Page**: Overview of the business with featured services and testimonials.
- **Portfolio**: Display of makeup and mehndi work categorized by type (Makeup, Mehendi, Bridal, Party).
- **Services**: List of available services with descriptions and images.
- **Booking System**: Users can book appointments for services, including date, time, and contact details.
- **Contact Form**: Allows users to submit inquiries or messages.
- **User Accounts**: Registration and login functionality for user management.
- **Admin Panel**: Django admin interface for managing content (services, portfolio, bookings, etc.).
- **Media Management**: Support for uploading and displaying images for services, portfolio, and testimonials.
- **Email Integration**: Configured for sending booking confirmations via email (using Mailtrap for testing).

## Technologies Used

- **Backend**: Django 5.1.3
- **Database**: SQLite (default), configurable to PostgreSQL or MySQL for production
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap for styling)
- **Media Handling**: Django's static and media files handling
- **Email**: SMTP via Mailtrap.io for development/testing

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (recommended: venv)

### Steps

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd MyDemo
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
   Note: If `requirements.txt` is not present, install Django manually:
   ```
   pip install django
   ```

4. **Apply migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```
   Access the site at `http://127.0.0.1:8000/`

## Usage

- **Home**: Visit the root URL to see the homepage.
- **Portfolio**: Navigate to `/portfolio/` to view the portfolio items.
- **Services**: Go to `/services/` to see available services.
- **Booking**: Use `/booking/` to make a booking. Fill in the form and submit.
- **Contact**: Use `/contact/` to send a message.
- **Admin**: Access `/admin/` with superuser credentials to manage content.

### Email Configuration

For production, update the email settings in `MyDemo/settings.py`:
- Replace Mailtrap credentials with your SMTP provider (e.g., Gmail, SendGrid).
- Uncomment and configure the production email backend.

## Models

### Home App Models

- **Service**: Represents a service offered (title, description, image).
- **Portfolio**: General portfolio items (title, image, description).
- **PortfolioItem**: Categorized portfolio items (Makeup, Mehendi, etc.) with category choices.
- **Testimonial**: Client testimonials (name, content, image).
- **Booking**: Booking records (name, email, phone, service, date, time).
- **ContactSubmission**: Contact form submissions (name, email, message).

### Accounts App Models

- Uses Django's built-in User model for authentication.

## Project Structure

```
MyDemo/
├── MyDemo/                 # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/                   # Home app for main content
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── accounts/               # Accounts app for user management
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── public/                 # Static files
├── media/                  # Uploaded media files
├── db.sqlite3              # Database file
└── manage.py
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b main`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin main`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, contact [jaydeeppatidar2301@gmail.com].
