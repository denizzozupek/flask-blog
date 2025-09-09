from app.extensions import db
from flask_login import UserMixin
from datetime import datetime
from bs4 import BeautifulSoup

# Association table for many-to-many relationship
post_categories = db.Table('post_categories',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    categories = db.relationship('Category', secondary='post_categories', backref=db.backref('posts', lazy='dynamic'))

    @property
    def first_image(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        img_tag = soup.find('img')
        return img_tag['src'] if img_tag else None
    
    @property
    def excerpt(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        text = soup.get_text()
        return (text[:400] + '...') if len(text) > 400 else text
    
    @property
    def next_post(self):
        return Post.query.filter(Post.id > self.id).order_by(Post.id.asc()).first()
    
    @property
    def prev_post(self):
        return Post.query.filter(Post.id < self.id).order_by(Post.id.desc()).first()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)