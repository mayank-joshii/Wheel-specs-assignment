# 🚗 Wheel Specifications API Assignment

This Django-based backend API allows you to submit and retrieve wheel specifications. The project is configured with PostgreSQL and includes two main endpoints:

- `POST /api/forms/wheel-specifications` – Submit wheel specification data
- `GET /api/forms/wheel-specifications/lists` – Retrieve all wheel specification entries

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mayank-joshii/Wheel-specs-assignment.git
cd Wheel-specs-assignment
2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure PostgreSQL Database
Create a new PostgreSQL database (e.g., wheel_specs_db) using pgAdmin or psql.

Then update the DATABASES section in settings.py:
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
6. Run the Development Server
python manage.py runserver


NOTE : Use the URL as stated in the url patterns ( Eg. - api/forms/wheel-specifications and api/forms/wheel-specifications/lists )
