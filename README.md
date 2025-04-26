# 🛡️ Process Monitor System

A complete web-based system to monitor system processes on a machine in real-time!

Built with:
- Python Agent (EXE)
- Django REST API Backend
- Interactive Frontend (DataTables + Expand/Collapse)
- SQLite Database

---

## ✨ Features

- Collects Process Info: PID, Name, CPU%, Memory%, Parent
- Sends data from Agent to Django REST API
- Displays processes in an expandable/collapsible tree structure
- CPU/Memory usage shown with colorful progress bars
- Searchable, sortable, paginated view
- Authentication using API Key
- Mobile and desktop responsive

---

## 🛠️ Tech Stack

- Python 3
- Django 4
- Django REST Framework
- psutil (for agent-side system info)
- requests (agent-side HTTP)
- HTML5, CSS3
- JavaScript, jQuery
- DataTables.js

---

## 🚀 How to Run

### 1. Backend - Django Server

Install required Python libraries:

```bash
pip install -r requirements.txt
```

Migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

---

### 2. Agent (Python Script)

Run the agent manually:

```bash
python agent.py
```

or Compile to `.exe`:

```bash
pyinstaller --onefile agent.py
```
> Output `.exe` will be available in `dist/agent.exe`.

---

### 3. Frontend (Website)

- Visit: `http://127.0.0.1:8000/`
- Enter your hostname (as detected by the agent)
- View processes, expand/collapse subprocesses, monitor CPU/Memory usage visually!

---

## 🔐 Authentication

The Agent must send a **valid API key**:
- Format: `Authorization: Token your-api-key`
- Backend validates the token before accepting process data.

---

## 🗂️ Project Structure

```
project/
├── agent/
│   └── agent.py
├── process_monitor/
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   └── monitor/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── auth.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 📚 Documentation

### 📈 Architecture Diagram

```
[Agent (.exe)] --> [POST /api/process-data/] --> [Django Backend (SQLite)]
                                                       ↓
                                               [Frontend UI fetches /api/view-processes/?hostname=]
                                                       ↓
                                              [Interactive Web Table (Expand/Collapse)]
```

---

### 📑 API Endpoints

#### ➡️ POST `/api/process-data/`

- Headers:
  - `Authorization: Token your-api-key`
- Body:

```json
{
  "hostname": "MyPC",
  "processes": [
    {
      "pid": 1234,
      "name": "python.exe",
      "cpu": 5.2,
      "memory": 2.5,
      "parent_pid": 567,
      "parent_name": "explorer.exe"
    }
  ]
}
```

- Response:

```json
{"status": "success"}
```

---

#### ➡️ GET `/api/view-processes/?hostname=MyPC`

- Returns latest 100 processes for that hostname
- Used by the frontend table

---

## 📷 Screenshots (Optional)

> (Paste screenshots of the frontend, process table expanded view here for final report.)

---

## 📦 Requirements.txt

```text
Django>=4.0
djangorestframework>=3.14.0
psutil>=5.9.0
requests>=2.25.0
```

---

## ✅ Status

- [x] Agent EXE ready
- [x] Backend API live
- [x] Frontend Table built
- [x] Expandable subprocesses working
- [x] CPU/Memory visualizations
- [x] Authentication working
- [x] Final Packaging Done

---

