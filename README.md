# 🧠 Brainwave Internship – Django Project

This is a Django-based web system developed as part of my **Brainwave Internship Task**.  
It demonstrates practical implementation of Django framework, admin panel setup, and database configuration.

---

## 🚀 Getting Started

Follow the steps below to set up and run the project on your local machine.

---

## 📦 Prerequisites

- ✅ Python (3.x recommended)  
- ✅ Django installed  
- ✅ MySQL (or SQLite if using default DB)  
- ✅ VSCode / PyCharm / Any preferred editor

---

## 🛠️ Setup Instructions

1. **Download or Clone this Repository**

```bash
git clone https://github.com/yourusername/brainwave-django-project.git
cd brainwave-django-project
Open the project folder in VSCode or your preferred IDE
Make sure you're in the folder where manage.py is located.

⚙️ Configure MySQL (Optional)
If you're using MySQL instead of SQLite:

Go to settings.py

Locate the DATABASES section

Update it like this:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
🔧 Apply Migrations and Create Superuser
<b>Run the following commands in your terminal:</b>

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
✅ Enter your username and password when prompted. Keep them safe for admin login.

▶️ Run the Server
python manage.py runserver
