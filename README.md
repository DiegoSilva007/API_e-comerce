# API E-commerce

A REST API for an e-commerce application, developed with **Python and Flask**, using **SQLite** for data persistence.

The project focuses on backend development, RESTful endpoints, user session management, product management, and shopping cart operations.

## 🚀 Features

### Authentication

* User login
* User logout
* Session management with Flask-Login
* Protected endpoints requiring authentication

### Products

* Add products
* List all products
* Retrieve a specific product
* Update products
* Delete products
* Product name, price, and description

### Shopping Cart

* Add products to the cart
* List the current user's cart
* Remove products from the cart
* Checkout and clear the cart

## 🧩 Technologies

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLAlchemy ORM**
* **SQLite**
* **Flask-Login**
* **Flask-CORS**

## 🏗️ Architecture

The application follows a backend/API structure in which clients communicate with the Flask application through HTTP requests.

```text
Client
   │
   │ HTTP Requests
   ▼
Flask REST API
   │
   ├── Authentication
   ├── Products
   └── Shopping Cart
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite Database
```

## 📌 Main Endpoints

### Authentication

| Method | Endpoint  | Description             |
| ------ | --------- | ----------------------- |
| POST   | `/login`  | Authenticate a user     |
| POST   | `/logout` | End the current session |

### Products

| Method | Endpoint                            | Description            |
| ------ | ----------------------------------- | ---------------------- |
| GET    | `/api/products`                     | List all products      |
| GET    | `/api/products/<product_id>`        | Get a specific product |
| POST   | `/api/products/add`                 | Add a product          |
| PUT    | `/api/products/update/<product_id>` | Update a product       |
| DELETE | `/api/products/delete/<product_id>` | Delete a product       |

### Shopping Cart

| Method | Endpoint                        | Description                          |
| ------ | ------------------------------- | ------------------------------------ |
| POST   | `/api/cart/add/<product_id>`    | Add a product to the cart            |
| GET    | `/api/cart`                     | Get the current user's cart          |
| DELETE | `/api/cart/remove/<product_id>` | Remove a product from the cart       |
| POST   | `/api/cart/checkout`            | Complete checkout and clear the cart |

## 📚 What I Practiced

This project allowed me to practice:

* REST API development
* HTTP methods
* CRUD operations
* Flask application structure
* SQLAlchemy ORM
* Relational data modeling
* Database persistence with SQLite
* User session management
* Authentication with Flask-Login
* Protected API endpoints
* Frontend/backend communication concepts
* CORS configuration
* API testing and development

## 🔄 Future Improvements

Possible improvements for the project include:

- Secure password hashing
- User registration endpoint
- Better input validation
- More robust error handling
- Order persistence
- Automated tests
- Environment-based configuration
- More granular authorization
- Restricting CORS to trusted origins
- Production configuration without debug mode
- Production deployment

## 🎯 Project Objective

The main objective of this project was to build a practical backend application while developing my understanding of **REST APIs, databases, authentication, ORM, and backend architecture**.

The project can also serve as a foundation for further development into a more complete e-commerce system.

## 👨‍💻 Author

**Diego Silva**

Full Stack Developer | Software Engineering Student
