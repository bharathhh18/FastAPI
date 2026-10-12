# 🚀 FastAPI Learning Journey

### *Learning by building. Improving by debugging.*

Welcome to my FastAPI learning repository! 👋

This repository documents my journey of learning **FastAPI and backend development with Python**, with practical examples, experiments, and notes from my learning process.

## 📚 What I'm Learning

- ⚡ Creating a FastAPI application
- 🌐 Building GET endpoints
- 📦 Fetching all products
- 🔍 Retrieving individual products
- 🛣️ Understanding fixed and dynamic paths
- 🆔 Searching using actual product IDs
- ⚠️ Handling products that are not found

## 🛠️ Tech Stack

- 🐍 Python
- ⚡ FastAPI
- 🚀 Uvicorn
- 📝 VS Code

## 📂 Project Structure

```text
FastapiTelusko/
├── main.py
├── models.py
├── NOTES.md
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | FastAPI application and GET endpoints |
| `models.py` | Product model definition |
| `NOTES.md` | Detailed explanations of the code and concepts |
| `README.md` | Repository overview |

## ▶️ How to Run

**1. Install the dependencies**

```bash
pip install fastapi uvicorn
```

**2. Start the development server**

```bash
python -m uvicorn main:app --reload
```

**3. Explore the API**

Open `http://127.0.0.1:8000/docs` in your browser to test the available endpoints.

## 💡 What This Project Teaches

One important concept explored in this project is the difference between a **list index and a product ID**.

The product IDs are intentionally non-sequential, helping demonstrate why searching by the actual ID is different from accessing an item by its list position.

## 📈 Learning in Progress

This repository is part of my ongoing backend development learning journey. I'll continue adding concepts and practical examples as I progress.

---

⭐ *Small projects. Strong fundamentals. Consistent progress.*