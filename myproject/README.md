# WhatBytes Django Web Application with User Authentication

![Django Logo](https://www.djangoproject.com/s/img/logos/django-logo-negative.png)

## Features as mentioned in the Google Document

- [**User Registration:**](#user-registration) Allow users to create new accounts by providing their username, email, and password.
- [**User Login:**](#user-login) Enable registered users to log in **securely** using their credentials.
- [**Personalized Dashboard:**](#personalized-dashboard) Greet users with a personalized dashboard upon successful login.
- [**User Profile:**](#user-profile) Display basic user profile information, such as username and email address.
- [**Secure Logout:**](#secure-logout) Provide users with a secure logout option to end their session.

## URLs and Views

- **User Registration:** [/register/](http://127.0.0.1:8000/register/) - [views.register](#user-registration)
- **User Login:** [/login/](http://127.0.0.1:8000/login/) - [views.user_login](#user-login)
- **Personalized Dashboard:** [/dashboard/](http://127.0.0.1:8000/dashboard/) - [views.dashboard](#personalized-dashboard)
- **User Profile:** [/profile/](http://127.0.0.1:8000/profile/) - [views.profile](#user-profile)
- **Secure Logout:** [/logout/](http://127.0.0.1:8000/logout/) - [views.user_logout](#secure-logout)
- **Please Login:** [/please_login/](http://127.0.0.1:8000/please_login/) - [views.please_login](#please-login)

## Running the Application

### With Docker

1. **Clone the Repository:**
   ```
   git clone https://github.com/manthanoice/whatbytes.git
   cd myproject
   ```

2. **Run the docker container using the following command**
   ```
   docker-compose up --build
   ```

3. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8000` to access the application.

### Without Docker

1. **Clone the Repository:**
   ```
   git clone https://github.com/manthanoice/whatbytes.git
   cd myproject
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Django Development Server:**
   ```
   python manage.py runserver
   ```

4. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8000` to access the application.