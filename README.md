Gas Utility Consumer Service

Overview

This Django-based web application helps gas utility companies manage a high volume of customer service requests. It allows customers to submit service requests, track their request status, and manage their accounts. Additionally, customer support representatives can handle and respond to these requests efficiently.

Features

For Customers:

User Authentication: Signup, login, logout, and profile management.

Service Requests: Submit a new request with type selection, details, and file attachments.

Request Tracking: View the status, submission date, and resolution time of requests.

Account Management: View personal account details and service history.

For Customer Support Representatives:

Dashboard: View and manage service requests.

Ticket System: Handle and respond to customer requests.

User Management: Access customer details and request history.
Project Structure:

gas_utility/
├── gas_utility/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── service_requests/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── service_requests/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── request_detail.html
│   │       └── submit_request.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/
├── manage.py
└── requirements.txt



Installation and Setup

Prerequisites

Python 3.9+

PostgreSQL installed and running

Django installed

Steps

Clone the repository:

git clone <repository_url>
cd gas_utility_service

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure PostgreSQL database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gas_utility_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Apply migrations and create superuser:

python manage.py migrate
python manage.py createsuperuser

Run the development server:

python manage.py runserver

Access the application:

Customer portal: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/
