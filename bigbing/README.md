# ✈️ AirSwift — Flight Management System

A web-based flight management system built with Django. Users can browse available flights, view passengers, submit feedback, and manage bookings through a clean, minimal interface.

---

## 🚀 Features

- User authentication (login/logout)
- Browse available flights by origin and destination
- View passengers on each flight
- Submit and view feedback
- Contact page
- Responsive dark UI

---

## 🛠️ Tech Stack

- **Backend** — Python, Django
- **Frontend** — HTML, CSS, Django Templates
- **Database** — SQLite 

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/dp0000000004-eng/prac-django
cd prac-django
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```
bigbing/
├── mesy/                  # Main app
│   ├── models.py          # Flight, Passenger, Feedback models
│   ├── views.py           # All views
│   ├── urls.py            # URL routes
│   ├── templates/mesy/    # HTML templates
│   └── static/mesy/       # CSS files
├── manage.py
└── requirements.txt
```


## 👤 Author

**Debasish Pradhan**  
CS Student | Python & Django Developer  
[LinkedIn](www.linkedin.com/in/debasish-p-d1) 

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
