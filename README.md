# Medical Crisis Management System

A Django-based web application for coordinating emergency medical response. The platform helps users report incidents and quickly find hospitals, ambulances, and police support, while administrators manage operational data such as hospitals, departments, doctors, staff, and emergency resources.

## Project Overview
This project centralizes medical crisis operations into one workflow:

1. Users register and log in.
2. Users report accidents and submit complaints.
3. Users search nearby support resources (hospital, ambulance, police).
4. Admin manages institutions and responders.
5. Admin monitors reported incidents and user complaints.

The application is built as a server-rendered Django app with MySQL as the backend database.

## Core Features
- Role-based login (`admin` and `user` roles).
- User registration and profile management.
- Hospital directory with details and services.
- Ambulance and police lookup by location.
- Accident reporting with type, location, date, and time.
- Complaint registration and admin-side complaint review.
- Admin management for hospitals, doctors, staff, departments, ambulances, and police records.

## Technology Stack
- Backend: Django 5.x (Python)
- Frontend: Django Templates, HTML, CSS, Bootstrap-based assets
- Database: MySQL
- ORM: Django ORM
- Static/Media: Django static and media configuration

## Modules and Responsibilities
- `crisis` app: business logic, models, views, templates, URL mappings
- `medicalcrisis` project: global settings, root URLs, WSGI/ASGI entry points
- `DATABASE/db_medical_crisis.sql`: SQL dump for initializing database data
- `staticfiles/` and `crisis/static/`: frontend static assets
- `media/`: uploaded/served media files

## Data Model Summary
Main entities in `crisis/models.py`:

- `login`: stores username, password, role
- `user`: end-user profile linked to login
- `location`: location master table
- `department`: medical department master data
- `hospital`: hospital metadata and facilities
- `doctor`: doctor linked to hospital and department
- `staff`: hospital staff linked to department and hospital
- `ambulance`: ambulance contact and location
- `police`: police contact and location
- `accident`: accident reports linked to user, location, and police
- `complaint`: user complaints

## URL Routes (High Level)
Defined in `crisis/urls.py`:

- Public/Auth: `/`, `/index`, `/login`, `/logout`
- Admin Dashboard and management pages: `/admin`, `/adminHospitalList`, `/adminDoctorList`, etc.
- User pages: `/user`, `/userRegister`, `/userSearchHospital`, `/userReportAccident`, etc.
- Profile and privacy: `/profile`, `/privacy`

## Project Structure
```text
medicalcrisis/
|-- crisis/
|   |-- templates/
|   |-- static/
|   |-- models.py
|   |-- views.py
|   `-- urls.py
|-- medicalcrisis/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- asgi.py
|-- DATABASE/
|   `-- db_medical_crisis.sql
|-- staticfiles/
|-- media/
|-- manage.py
|-- requirements.txt
`-- Procfile
```

## Prerequisites
- Python 3.10+
- MySQL Server
- `pip`
- Git (optional)

## Installation and Setup
From the project directory (`medicalcrisismca/medicalcrisis`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Database Setup
1. Create database in MySQL:

```sql
CREATE DATABASE db_medical_crisis;
```

2. Import dump file:

```powershell
mysql -u root -p db_medical_crisis < DATABASE\db_medical_crisis.sql
```

3. Verify database settings in `medicalcrisis/settings.py`:
`ENGINE = django.db.backends.mysql`
`NAME = db_medical_crisis`
`HOST = localhost`
`PORT = 3306`
Update `USER` and `PASSWORD` for your environment.

## Run the Project
```powershell
python manage.py check
python manage.py runserver 127.0.0.1:8000
```

Open in browser:

`http://127.0.0.1:8000/`

## Default Access (If Using Provided SQL Dump)

https://github.com/user-attachments/assets/ef57bab0-053e-47a5-8c77-d0090cdd2710


- Admin password: `admin`

If credentials were changed in your DB, use the updated values.

## Configuration Notes
- Local development currently uses `DEBUG = True`.
- For production, set `DEBUG = False` and configure secure `ALLOWED_HOSTS`, secret management, and static file serving.

## Common Troubleshooting
1. `ERR_CONNECTION_REFUSED`  
Ensure `python manage.py runserver 127.0.0.1:8000` is running in terminal.  
If port 8000 is busy, try: `python manage.py runserver 127.0.0.1:8001`.
2. Login shows invalid credentials  
Confirm user exists in `login` table and has role `admin` or `user`.
3. Styles not loading  
Ensure static paths are correct and keep `DEBUG = True` during local development.



## License
This project is currently for academic/project use. Add a formal license if you plan public distribution.
# MEDICALCRISIS
