import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.getenv("DATABASE_PATH")
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Upload settings
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}