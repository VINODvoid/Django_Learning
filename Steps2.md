# Setting Up Your Django Project

### Step 1: Create a New Django Project
Navigate to the directory where you want to create your project and run:

```bash
django-admin startproject myproject
```
### Step 2: Navigate to Your Project Directory
Change into the directory of your newly created project:

```bash
cd myproject
```
---
### Step 3: Run the Development Server
Start the Django development server to run your project locally. This allows you to view your Django project in a web browser.

```bash
python manage.py runserver
```
**Output** : 
```bash
Visit http://127.0.0.1:8000/ in your web browser to see your Django project running locally.
```
---
### Step 4: Create Your First App
Create a new Django app within your project. 
An app is a Web application that does something – e.g., a Weblog system, a database of public records, a simple poll app, etc.

```bash

python manage.py startapp myapp
```
Replace __myapp__ with the name of your app.
---
### Step 5: Define Your Models
Define your data models in the models.py file of your app. Models define the structure of your data and are used to create database tables.

---
### Step 6: Create Database Tables
Run migrations to create database tables for your models. Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

```bash
python manage.py makemigrations
python manage.py migrate
```
---
### Step 7: Create a Superuser
Create a superuser account to access the Django admin interface. The admin interface is a built-in feature of Django that provides a user-friendly interface for managing your site’s data.

```bash

python manage.py createsuperuser
```
Follow the prompts to set up your superuser account.

---
### Step 8: Start Building Your App!
You're all set to start building your Django app! Refer to the Django documentation for further guidance.

---


**Happy Coding!** :smiley:
Developed with ❤️ by ~~Kalki~~.

---
