# Flask Blog

Personal blog built with **Flask**, featuring posts, categories, an admin panel, backup functionality, image upload, and search.

## 🚀 Features
- User authentication (login/logout)
- Admin panel for managing posts and categories
- Post creation with image upload
- Categories system
- Full-text search
- Database backup
- Responsive design (HTML, CSS, JS)

## 🛠️ Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL (configurable)
- **Other:** Flask-Login, Werkzeug, Bootstrap

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/denizzozupek/flask-blog.git
   cd flask-blog
   
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
3. Install dependencies:
  pip install -r requirements.txt

4. Set up environment variables (see .env.example):
   cp .env.example .env
   
5.Run the application:
   flask run (run.py)

## ⚙️ Configuration

DATABASE_URL: PostgreSQL connection string

SECRET_KEY: Flask session key

ADMIN_USERNAME / ADMIN_PASSWORD: Admin panel login credentials

## 📂 Project Structure

flask-blog/
│── app/             # Main application package
│   ├── models.py    # Database models
│   ├── routes/      # Route definitions
│   ├── templates/   # HTML templates
│   └── static/      # CSS, JS, Images
│
│── config.py        # Config settings
│── run.py           # App entry point
│── requirements.txt # Dependencies
│── .env.example     # Environment variables template
│── wsgi.py          # WSGI entry point

📝 License

This project is licensed under the MIT License.
