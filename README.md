# Wheel Specifications Assignment – API Implementation

This project implements two REST API endpoints using Django and PostgreSQL to manage wheel specification data as part of the Suvidhaen KPA Assignment.

## ✅ Features Implemented

- **POST /api/forms/wheel-specifications/**  
  Allows submission of wheel specification data with various measurement fields.

- **GET /api/forms/wheel-specifications/list**  
  Returns a list of all submitted wheel specifications in JSON format.

## 📦 Tech Stack

- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Testing Tool**: Postman

---

## ⚙️ Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/mayank-joshii/Wheel-specs-assignment.git
   cd Wheel-specs-assignment
2. Create and Activate Virtual Environment
'''bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Configure PostgreSQL Database

Create a new database (e.g., wheel_specs_db) using pgAdmin or psql
In settings.py, update the DATABASES section with your PostgreSQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wheel_specs_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate


6. Run Development Server
python manage.py runserver


NOTE : Use the URL as stated in the url patterns ( Eg. - api/forms/wheel-specifications and api/forms/wheel-specifications/lists )
