# Staff Leave Management System

## Overview

The **Staff Leave Management System** is a Django-based web application that simplifies the process of managing employee leave requests. It provides separate interfaces for administrators and staff members, allowing staff to apply for leave while enabling administrators to review, approve, or reject requests efficiently.

The application uses **SQLite3** as the default database and follows the Django MVT (Model-View-Template) architecture.

---

# Features

- Staff Registration and Login
- Admin Login
- Apply for Leave
- View Leave Status
- Leave Approval and Rejection
- Staff Management
- Leave History
- Dashboard
- Authentication System
- Responsive User Interface
- Form Validation

---

# Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- SQLite3
- Django Templates

---

# Project Structure

```
Staff-Leave-Management-System/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── leave/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── static/
│
├── templates/
│
├── slms_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# Application Modules

## Authentication

Provides secure login functionality for Admin and Staff users.

### Functionalities

- Admin Login
- Staff Login
- Logout
- Session Management

---

## Admin Dashboard

Displays an overview of the leave management system.

### Functionalities

- View Total Staff
- View Total Leave Requests
- View Pending Requests
- View Approved Requests
- View Rejected Requests

---

## Staff Management

Allows administrators to manage staff information.

### Functionalities

- Add Staff
- Edit Staff Details
- Delete Staff
- View All Staff

---

## Leave Application

Allows staff members to submit leave requests.

### Leave Information

- Leave Type
- Start Date
- End Date
- Number of Days
- Leave Reason

### Validation

- All required fields must be completed.
- Start date cannot be after the end date.
- Leave reason cannot be empty.

---

## Leave Management

Allows administrators to manage all leave applications.

### Functionalities

- View Leave Requests
- Approve Leave
- Reject Leave
- View Leave Details
- Track Leave Status

---

## Leave History

Displays previous leave requests submitted by staff.

### Information Displayed

- Leave Type
- Applied Date
- Start Date
- End Date
- Reason
- Status

---

# Database

The project uses **SQLite3** as the default database.

Main tables include:

- Staff
- Leave Applications
- Authentication (Django User)

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/Staff-Leave-Management-System.git
```

Move into the project directory.

```bash
cd Staff-Leave-Management-System
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser.

```bash
python manage.py createsuperuser
```

Run the development server.

```bash
python manage.py runserver
```

Open your browser.

```
http://127.0.0.1:8000/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

# Usage

## Staff

### Login

Login using your staff credentials.

### Apply Leave

- Select Leave Type
- Choose Start Date
- Choose End Date
- Enter Reason
- Submit Application

### View Leave Status

Monitor whether your leave request is:

- Pending
- Approved
- Rejected

---

## Administrator

### Manage Staff

- Add Staff
- Edit Staff
- Delete Staff

### Manage Leave Requests

- View all applications
- Approve leave
- Reject leave
- Track leave history

---

# Future Enhancements

- Email Notifications
- Leave Balance Calculation
- Department-wise Leave Reports
- Role-Based Access Control
- Attendance Management Integration
- Payroll Integration
- REST API Development
- Mobile Responsive Design Improvements
- PDF and Excel Report Generation
- Multi-Level Leave Approval
- Calendar View for Leave Schedule

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Django Framework
- Python Programming
- Django MVT Architecture
- Django Authentication
- CRUD Operations
- Form Validation
- Session Management
- URL Routing
- SQLite Database
- Django ORM
- Model Relationships
- Template Inheritance
- Static Files Management
- Bootstrap Integration
- User Authentication
- Leave Workflow Management

---

# Screens

- Home Page
- Login Page
- Admin Dashboard
- Staff Dashboard
- Staff Management
- Leave Application Form
- Leave Requests
- Leave History
- Leave Approval Page

---

# Author

**Raghu Charan R A**

Built as a **Django web application** to practice authentication, CRUD operations, database management, Django ORM, template rendering, leave management workflow, and full-stack web development.
