# ⚡ FastAPI Product API

A REST API built with **Python and FastAPI** to explore backend development, HTTP methods, routing, and product data management.

## 📌 Overview

This project implements a product API with endpoints to retrieve product information and fetch the complete product collection. It focuses on API design, request handling, and working with structured product data.

## ✨ Features

- 📦 Retrieve all available products.
- 🔍 Fetch individual products using their IDs.
- 🛣️ Implement fixed and dynamic API routes.
- ⚠️ Handle requests for products that do not exist.
- 🧩 Define structured product models using Python.
- 🧪 Test endpoints using interactive API documentation.

## 🛠️ Tech Stack

- 🐍 **Python** — Core programming language
- ⚡ **FastAPI** — API development framework
- 🚀 **Uvicorn** — ASGI server
- 💻 **VS Code** — Development environment

## 📂 Project Structure

```text
FastapiTelusko/
├── main.py       # API routes and application logic
├── models.py     # Product data model
├── NOTES.md      # Technical notes and explanations
└── README.md     # Project documentation
```

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

### 2️⃣ Start the Development Server

```bash
python -m uvicorn main:app --reload
```

### 3️⃣ Explore the API

Open the following URLs in your browser:

- 📖 **Interactive API Docs:** http://127.0.0.1:8000/docs
- 🌐 **Local Server:** http://127.0.0.1:8000

Use the interactive documentation to test the available endpoints.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/products` | Retrieve all products |
| `GET` | `/products/{id}` | Retrieve a product by ID |

## 📈 What's Next?

This project is a foundation for exploring REST API development with FastAPI. Future improvements will include:

- ➕ Creating products using `POST`
- ✏️ Updating products using `PUT`
- 🗑️ Deleting products using `DELETE`
- 🗄️ Integrating a database for persistent storage
- ✅ Improving request validation and error handling

---

🚧 **Status:** Actively learning and developing.

⭐ *Building practical projects. Strengthening backend fundamentals.*