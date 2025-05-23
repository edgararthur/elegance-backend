# E-commerce Backend API

This is the backend API for the e-commerce product page application built with Django and Django REST Framework.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register a new user
- `POST /api/users/login/` - Login and get token
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile

### Products
- `GET /api/products/` - List all products
- `GET /api/products/{slug}/` - Get product details
- `GET /api/products/featured/` - Get featured products
- `GET /api/products/new_arrivals/` - Get new arrival products
- `GET /api/products/categories/` - List all categories
- `GET /api/products/categories/{slug}/` - Get category details
- `GET /api/products/category/?slug={category_slug}` - Get products by category

### Orders
- `GET /api/orders/` - List user orders
- `POST /api/orders/` - Create a new order
- `GET /api/orders/{id}/` - Get order details

## Models

### Products
- Category: Product categories
- Product: Product information
- ProductImage: Images associated with products

### Orders
- Order: Order information
- OrderItem: Individual items in an order

### Users
- UserProfile: Extended user profile information

## Authentication

The API uses token-based authentication. Include the token in the Authorization header:
```
Authorization: Token <your-token>
``` #   e l e g a n c e - b a c k e n d  
 