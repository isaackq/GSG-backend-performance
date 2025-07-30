# 🧩 Simple Flask Todo API

This is a lightweight RESTful API built using **Python** and **Flask**, designed to demonstrate basic endpoint implementation and performance testing.

The API stores data **in memory** (not persisted), and supports basic todo-style operations:

- `GET /items` – return a list of items
- `POST /items` – add a new item to the list

---

## 📁 Project Structure

```
TEST_FOLDER/
│
├── Report.pdf          # 1-page performance & testing report
├── screenshots         # screenshots of the performed tests
├── app.py              # Main Flask app (GET/POST logic)
├── Dockerfile          # Docker setup to run the app in a container
├── requirements.txt    # Python dependencies (Flask + basic libs)
├── sql-lite-test.py    # Optional: SQLite to do test performance without im memory storage
└── README.md           # Project documentation (this file)
```

---

## ⚙️ Requirements

### For local (non-Docker) setup:

- Python 3.10 or higher
- pip

### For Docker setup:

- Docker (v20+ recommended)

---

## 📥 Clone & Navigate to Project

```bash
git clone <repo-link>
```

```bash
cd GSG-backend-performance
```

---

## ▶️ Run Locally with Python

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Run the app**:

```bash
python app.py
```

3. **Access the API**:
   Visit `http://localhost:5000/items` using a browser or Postman or curl.

---

## 🐳 Run Using Docker

1. **Build the Docker image**:

```bash
docker build -t flask-api .
```

2. **Run the container**:

```bash
docker run --rm -p 5000:5000 flask-api
```

3. **Access via**:

```
http://localhost:5000/items
```

---

## 📡 API Endpoints

### `GET /items`

Returns the current list of todo items.

### `POST /items`

Adds a new item. JSON body example:

```json
{
  "name": "Do homework"
}
```

---

## 🖋️ Report

You can read the report in [API_Report.txt](./API_Report.txt)

## 📌 Notes

- Data is stored in RAM, so restarting clears all items.
