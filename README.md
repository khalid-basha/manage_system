# manage_system
A Django project that implements a school system app that includes courses, teachers and students, as well as the relations between them. The project uses the Django Rest Framework for API creation and management.

## Requirements
- Python 3.7 or later.
- Django 4.1.3 or later.
- Django Rest Framework.
- Phonenumber_field.

## Installation

1. Clone the repository and navigate to the directory:
    ```
    git clone https://github.com/khalid-basha/manage_system.git
    cd manage_system/manage_system
    ```
    
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    
3. Run migrations to create the database and tables:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
   or <sub>depinde on python version you use<sub>
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
   
4. Create a superuser to access the admin panel:
    ```
    python manage.py createsuperuser
    ```
5. Start the development server:
    ```
    python manage.py runserver
    ```
    
## Usage
  The project contains the following apps:
  
  * school_system: The main app that contains models for courses, teachers and students, as well as their relationships.The models are as follows:
    + Course: A course that a student can enroll in. Each course has a name, subject, and full course hours.
    + Teacher: A teacher who teaches one or more courses. Each teacher has a first name, last name, email, and phone number.
    + Student: A student who can enroll in one or more courses. Each student has a first name, last name, email, and phone number.
  * rest_framework: The Django REST framework app for building APIs.
  * phonenumber_field: An app for handling phone number fields in the models.
  
  To access the admin panel, navigate to `http://localhost:8000/admin` and use the superuser credentials created in the installation step.
  To access the API, navigate to `http://localhost:8000/` and use the endpoint URLs to retrieve or modify data. For example, `http://localhost:8000/courses/` retrieves a list of all courses.
  
  ## Tests
  To run the tests for the project, use the `python manage.py test` command. This command will run the tests for all installed apps.
  
  ## Contributing
To contribute to the project, follow these steps:

1. Fork the repository and clone it to your local machine.

2. Create a new branch for your changes.

3. Make the changes and commit them to your branch.

4. Push the branch to your forked repository.

5. Create a new pull request against the main repository.

## References
* Django: https://www.djangoproject.com/
* Django REST framework: https://www.django-rest-framework.org/
* phonenumber_field: https://github.com/stefanfoulis/django-phonenumber-field
* Python 3.8: https://www.python.org/downloads/release/python-380/
