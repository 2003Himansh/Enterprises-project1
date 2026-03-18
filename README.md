# Enterprise E-Commerce Platform

A production-ready enterprise backend application built using FastAPI, demonstrating modern software development practices including clean architecture, authentication, logging, testing, and API documentation.

---

## Features

* High-performance REST API using FastAPI
* JWT-based Authentication
* Clean Architecture (Services, Models, Schemas)
* Database Integration (SQLAlchemy + SQLite)
* Logging and Middleware Support
* Unit Testing with Pytest
* Auto API Documentation (Swagger UI)
* CORS and Security Middleware
* Health Check Endpoint

---

## Project Structure

```
enterprise_project/
│
├── main.py
├── config.py
├── database.py
│
├── models.py
├── schemas.py
├── services.py
├── middleware.py
│
├── requirements.txt
├── .env
│
├── logs/
│   └── app.log
│
└── tests/
    └── test_main.py
```

---

## Installation and Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/enterprise-ecommerce-platform.git
cd enterprise-ecommerce-platform
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Application

```
uvicorn main:app --reload
```

---

## API Documentation

After running the server, open:

http://127.0.0.1:8000/docs

---

## Authentication

This project uses JWT token-based authentication.

Example header:

```
Authorization: Bearer {"id":1}
```

---

## API Endpoints

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | /health   | Health check     |
| GET    | /products | Get all products |
| POST   | /products | Create product   |
| POST   | /orders   | Create order     |

---

## Running Tests

```
pytest
```

---

## Logging

Logs are stored in:

```
logs/app.log
```

Includes API request logs, response time tracking, and errors.

---

## Security Features

* JWT Authentication
* CORS Protection
* Trusted Host Middleware
* Basic Rate Limiting

---

## Future Enhancements

* Docker and Kubernetes Deployment
* Cloud Deployment (AWS, Render)
* PostgreSQL with migrations
* Redis caching
* Monitoring with Prometheus and Grafana
* Full authentication system (login and register)

---

## License

This project is licensed under the MIT License.

---

## Career Impact

This project demonstrates backend development, API design, DevOps basics, testing, and production-level coding practices.
