# E-commerce Django REST API Project

## Project Overview

This project is a Django REST API for an e-commerce platform that includes user registration, login, and logout functionalities using Simple JWT. It also implements a role-based access control system where only admins can add products to the site. The API allows for fetching all products, adding products, add products to cart, generating billing, and handling payments through the Stripe library.

## Features

- User Registration
- User Login and Logout
- Role-based Access Control
- Only admins can add products
- Fetch all products
- Add products (Admin only)
- Generate billing
- Payment processing using Stripe

## Technologies Used

- Django
- Django REST Framework
- Simple JWT for authentication
- PostgreSQL for the database
- Stripe for payment processing

## API Endpoints

### Authentication

- **Register User**: `/users/register/`
- **Login**: `/users/token/`
- **Logout**: `/users/logout/`

### Products

- **Fetch All Products**: `/products/list/`
- **Fetch Single Product**: `/products/list/<id>`
- **Add Product**: `/products/add/` (Admin only)

### Billing and Payments

- **Generate Billing**: `/profiles/`
- **Process Payment**: `/checkout/hook/`

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- Stripe Account

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/rjcoder86/Django-Ecommerce
   cd django-ecommerce
   ```

2. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Update the DATABASES setting in settings.py to match your PostgreSQL configuration.

   ```DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql_psycopg2',
   'NAME': 'your_db_name',
   'USER': 'your_db_user',
   'PASSWORD': 'your_db_password',
   'HOST': 'your_db_host',
   'PORT': 'your_db_port',
   }
   }
   ```

4. **Run database migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Configure Stripe:**

Add your Stripe API keys to settings.py:

```python
STRIPE_SECRET_KEY = 'your_secret_key'
STRIPE_PUBLISHABLE_KEY = 'your_publishable_key'
```

Run the development server:

```sh
python manage.py runserver
```

## Usage

### Register User

- **Endpoint**: `/users/register/`
- **Method**: `POST`
- **Request Body**:

```json
{
  "full_name": "first_name last_name",
  "email": "user@gmail.com",
  "password": "password",
  "phone": "1236547890"
}
```

### Login

**Endpoint**: `/users/login/`
**Method**: `POST`
**Request Body**:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### Logout

- **Endpoint**: `/users/logout/`
- **Method**: `POST`
- **Request Body**:

```json
{
  "refresh": "your_refresh_token"
}
```

### Fetch All Products

- **Endpoint**: `/products/list/`
- **Method**: `GET`

### Add Product (Admin only)

- **Endpoint**: `/products/add/`
- **Method**:` POST`
- **Request Body**:

```json
{
  "title": "Product title ",
  "description": "This is a dummy product for testing purposes.",
  "original_price": 200.0,
  "price": 80.0,
  "tax": 18.0
}
```

### Add to Cart

- **Endpoint**: /cart/
- **Method**: POST
- **Request Body**:

```json
{
  "id": "product id",
  "quantity": 2
}
```

### Generate Billing

- **Endpoint**: /billing/
- **Method**: POST
- **Request Body**:

```json
{
  "name": "username",
  "email": "user email",
  "address_line_1": "203 shanti niwas",
  "address_line_2": "Phulera",
  "city": "Phakoli",
  "state": "MP",
  "country": "India",
  "pincode": "123654"
}
```

### Process Payment

- **Endpoint**: /checkout/hook/
- **Method**: POST
- **Request Body**:

```json
{
  "id": "event id",
  "object": "event",
  "api_version": "2020-08-27",
  "created": 1603248451,
  "data": {
    "object": {
      "id": "pi_1Fy3jV2eZvKYlo2C9Y7HJ2Oj",
      "object": "payment_intent",
      "amount": 2000,
      "currency": "usd",
      "description": "Order Id <order id>",
      "status": "succeeded"
    }
  },
  "livemode": false,
  "pending_webhooks": 1,
  "request": {
    "id": null,
    "idempotency_key": null
  },
  "type": "payment_intent.succeeded"
}
```

### Contributing

Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
