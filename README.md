Django Project with DRF and Swagger

Introduction
This Django project serves as a boilerplate for setting up a RESTful API using Django Rest Framework (DRF) with integrated Swagger documentation.

Features
User registration and authentication using JWT tokens.
Swagger/OpenAPI documentation for API endpoints.
Customization of UserModel and authentication serializer.

API Endpoints
http://127.0.0.1:8000
/register/: User registration endpoint.
http://127.0.0.1:8000/login/: User login endpoint to obtain JWT tokens.




1) Activate Virtual Environment:
Before running the Django project, make sure to activate your virtual environment. You can activate it using the following command:

myenv\Scripts\activate  # For Windows
source myenv/bin/activate  # For Linux/Mac

2) Install Dependencies:
Navigate to your project directory and install the required dependencies using pip:

pip install -r requirements.txt

3) Migrate Database:
Run the migrations to create database tables:

python manage.py migrate

4)Create Superuser (Optional):
If you want to access the Django admin panel, create a superuser:

python manage.py createsuperuser

5) Run Development Server:
Start the Django development server:

python manage.py runserver

6)Access APIs:
You can now access the REST APIs for user registration and login at the specified endpoints. Make sure to check the documentation or code comments for the API endpoints.

7) Test APIs:
Use tools like Postman or cURL to test the APIs. Register a user, obtain JWT tokens, and test the login functionality.

8)Admin Panel (Optional):
If you created a superuser, you can access the Django admin panel at http://127.0.0.1:8000/admin/ and login with your superuser credentials.

9)Documentation:
swagger is used for api documentation
