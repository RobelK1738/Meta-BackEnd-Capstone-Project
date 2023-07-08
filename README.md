# Description

This is the final assignment for the Backend Developer Capstone Course of the Meta Backend Developer Professional Certificate on Coursera.

# Project Structure

The project is composed of two apps: `api` and `restaurant`. The `api` app serves API endpoints of the project, while the `restaurant` app serves its frontend. The `config` directory holds the major settings of the project.

# Installation

Install the dependencies:

\```bash
pipenv install
\```

Activate the virtual environment:

\```bash
pipenv shell
\```

# Setup

The default database settings are:

\```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'admin',
        'PASSWORD': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
\```

💡 Change those settings according to your local setup.

Apply the migrations:

\```bash
python manage.py migrate
\```

# Environment Variables

For authenticated API requests in the view of the restaurant app, a username and password must be provided. Follow the instructions below:

Inside the restaurant app folder, create a file called `.env` and place the following code inside it:

\```plaintext
USERNAME=your_username
PASSWORD=your_password
\```

<aside>💡 Replace "your_username" and "your_password" with a valid username and password, respectively.</aside>

<aside>💡 Be aware that `django-environ` must be installed for this to work. Such dependency should be installed by running `pipenv install`.</aside>

# API Endpoints

The `api` app has a total of 4 endpoints. Additionally, `Djoser` and `SimpleJWT` endpoints are available.

Each endpoint requires a SimpleJWT Token for authorization. Pass the token in the header of the request such as:

\```jsx
{'Authorization': 'JWT <token>'}
\```

In Insomnia, add the token as follows:

![Insomnia](assets/insomnia.png)

### Endpoints for `api` app

- `http://127.0.0.1:8000/api/menu-items`
  - Method: GET
  - Action: Retrieves all menu items
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

- `http://127.0.0.1:8000/api/menu-items/{menu-itemId}`
  - Method: GET
  - Action: Retrieves the menu item details
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: PUT
  - Action: Update the menu item
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: PATCH
  - Action: Partially update the menu item
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: DELETE
  - Action: Delete the menu item
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

- `http://127.0.0.1:8000/api/bookings`
  - Method: GET
  - Action: Retrieves all bookings
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: POST
  - Action: Creates a booking
  - TOKEN AUTH: Yes
  - STATUS CODE: 201

- `http://127.0.0.1:8000/api/bookings/{bookingId}`
  - Method: GET
  - Action: Retrieves the booking details
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: PUT
  - Action: Update the booking
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: PATCH
  - Action: Partially update the booking
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

  - Method: DELETE
  - Action: Delete the booking
  - TOKEN AUTH: Yes
  - STATUS CODE: 200

### Endpoints for `djoser` app

- `http://127.0.0.1:8000/auth/users/`
  - Method: GET
  - Action: Retrieves all users
  - STATUS CODE: 200
  - TOKEN AUTH: No

  - Method: POST
  - Action: Creates a user
  - STATUS CODE: 201
  - TOKEN AUTH: No

💡 Please refer to the [Djoser documentation](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints) for further usage on these endpoints.

### Endpoints for `simplejwt` app

- `http://127.0.0.1:8000/api/token/login/`
  - Method: POST
  - Action: Generates access token and refresh token
  - TOKEN AUTH: Yes
  - STATUS CODE: 201

- `http://127.0.0.1:8000/api/token/refresh/`
  - Method: POST
  - Action: Generates a new access token
  - TOKEN AUTH: Yes
  - STATUS CODE: 201

# Testing

There are a total of 12 tests to ensure that each API endpoint and each of its allowed HTTP methods work properly.

Run the tests:

\```bash
python manage.py test
\```

The output should be something similar to this:
\```
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
Ran 12 tests in 6.024s

OK
Destroying test database for alias 'default'...
\```

<aside>💡 These tests intrinsically test the `restaurant` models by creating entries in its database through the Django ORM.</aside>
