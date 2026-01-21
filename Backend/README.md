# HRMS Lite – Backend
This repository contains the backend implementation of HRMS Lite, a lightweight Human Resource Management System built as part of a full‑stack coding assignment.

The backend is responsible for managing employee records and tracking daily attendance through clean, RESTful APIs. It is designed to be simple, stable, and production‑ready.

# Overview
HRMS Lite is a basic internal HR tool that allows an admin to:
* Add, view, and delete employees
* Mark daily attendance (Present / Absent)
* View attendance records per employee

The system assumes a single admin user and does not include authentication, payroll, or leave management features, as they are out of scope for this assignment.

# Using Tech Stack:
Backend Framework: Django
API Framework: Django REST Framework 
Database: PostgreSQL 
Deployment: Render
Language: Python 

## Feature
RESTful APIs for employee and attendance management

* Server‑side validations:

  * Required fields
  * Valid email format
  * Duplicate employee prevention
  * Duplicate attendance prevention (same employee & date)
* Meaningful HTTP status codes and error messages
* Environment‑based configuration using `.env`
* PostgreSQL integration for production use

## All APIs
### Employee APIs
 Method :     Endpoint          : Description        
 
 GET    : `/api/employees/`      : List all employees 
 POST   : `/api/employees/`      : Add a new employee 
 DELETE : `/api/employees/{id}/` : Delete an employee 

### Attendance APIs
 Method : Endpoint                         : Description                     

 POST   : `/api/attendance/`               : Mark attendance                 
 GET    : `/api/attendance/{employee_id}/`  :view attendance for an employee 


## Running the Project Locally
###  Clone the Repository
git clone <repository-url>
cd Backend

Create and Activate Virtual Environment

Create : python -m venv env
Activate : env/Scripts/activate

Install Dependencies:pip install -r requirements.txt

###  Environment Variables
Create a `.env` file in the project root:

.env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://postgres:password@localhost:5432/hrms_db

Run Migrations:
python manage.py makemigrations
python manage.py migrate

Run the Server Localy: python manage.py runserver
Backend will be available at: http://127.0.0.1:8000/


Deployment : on Render using
* Render Web Service for Django API
* Render Managed PostgreSQL database

The application uses environment variables provided by Render, including `DATABASE_URL`, ensuring a secure and scalable production setup.

## Assumptions & Limitations
* Single admin user (no authentication)
* No role‑based access
* No leave, payroll, or reporting modules
* Designed for internal use only

Author : Saddam Hussain Mansuri