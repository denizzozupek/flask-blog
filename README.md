
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
   
   git clone https://github.com/denizzozupek/flask-blog.git
   cd flask-blog


2. Create a virtual environment and activate it:

   
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   

3. Install dependencies:

   
   pip install -r requirements.txt
  

4. Set up environment variables (see .env.example):

  
   cp .env.example .env
  

5. Run the application:

   
   flask run
   

## ⚙️ Configuration

* **DATABASE\_URL:** PostgreSQL connection string
* **SECRET\_KEY:** Flask session key
* **ADMIN\_USERNAME / ADMIN\_PASSWORD:** Admin panel login credentials

## 📂 Project Structure

```markdown
- flask-blog/
  - app/             # Main application package
    - models.py      # Database models
    - routes/        # Route definitions
    - templates/     # HTML templates
    - static/        # CSS, JS, Images
  - config.py        # Config settings
  - run.py           # App entry point
  - requirements.txt # Dependencies
  - .env.example     # Environment variables template
  - wsgi.py          # WSGI entry point
```


## 📷 Screenshots

<div style="text-align: center;">
  <img width="1892" height="690" alt="image" src="https://github.com/user-attachments/assets/f80e66ad-4921-45fb-9c62-cfce47bef100" />
  <br><br>
  <img width="1903" height="912" alt="Screenshot_1" src="https://github.com/user-attachments/assets/f469e13e-56ad-4790-a91b-230cd250ffaa" />
  <br><br>
  <img width="390" height="623" alt="Screenshot_2" src="https://github.com/user-attachments/assets/58f1b1c9-438e-4237-b06f-ef788a3c346a" />
</div>
  


</p>

📝 License

This project is licensed under the MIT License.




