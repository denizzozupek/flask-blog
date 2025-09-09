import os
import re
import html
from markupsafe import Markup
from bs4 import BeautifulSoup
from PIL import Image
from werkzeug.utils import secure_filename
from sqlalchemy import inspect

AY_ISIMLERI = [
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
]

def format_turkish_date(value):
    return f"{value.day} {AY_ISIMLERI[value.month - 1]} {value.year}"

def process_post_content(content):
    """1. <p> içindeki <img> etiketlerini çıkarır. 2. Düz metni <p> içine sarar."""
    parts = re.split(r'(<img .*?/?>)', content, flags=re.IGNORECASE)
    new_content = ''
    for part in parts:
        if part.lower().startswith('<img'):
            new_content += part
        else:
            text = part.strip()
            if text:
                new_content += f'<p>{text}</p>'
    return Markup(new_content)

def fix_image_src(content):
    soup = BeautifulSoup(content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not src.startswith('/'):
            img['src'] = '/' + src.lstrip('/')
    return str(soup)

def allowed_file(filename):
    from flask import current_app
    ALLOWED_EXTENSIONS = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_image(filepath):
    try:
        img = Image.open(filepath)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False

def create_default_categories():
    from app.models import Category
    from app.extensions import db
    
    categories = ['Bilim', 'Tarih', 'Felsefe', 'Film', 'Dizi', 'Kitap', 'Oyun']
    if not Category.query.first():
        db.session.add_all([Category(name=cat) for cat in categories])
        db.session.commit()

def backup_posts():
    from app.extensions import db
    
    inspector = inspect(db.engine)
    if inspector.has_table("post"):
        import pandas as pd
        df = pd.read_sql_table('post', db.engine)
        df.to_csv('backup_posts.csv', index=False)