import os
import time
import pandas as pd
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from app.admin import bp
from app.models import User, Post, Category
from app.extensions import db
from app.utils import fix_image_src, allowed_file, is_image
from flask import jsonify


@bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin.admin_dashboard'))
        else:
            flash("Invalid username or password", "error")
    return render_template('admin_login.html')

@bp.route('/logout')
@login_required
def admin_logout():
    logout_user()
    flash("Başarıyla çıkış yapıldı.", "success")
    return redirect(url_for('admin.admin_login'))

@bp.route('/')
@login_required
def admin_dashboard():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('admin_dashboard.html', posts=posts)

@bp.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    categories = Category.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if not title or not content:
            flash("Başlık veya içerik boş olamaz!", "error")
            return redirect(url_for('admin.new_post'))
        
        content = fix_image_src(content)
        new_post = Post(title=title, content=content)
        selected_categories = request.form.getlist('categories')
        new_post.categories = Category.query.filter(Category.id.in_(selected_categories)).all()
        db.session.add(new_post)
        db.session.commit()
        flash("Yeni gönderi başarıyla eklendi!", "success")
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('post_form.html', button_text='Yeni Gönderi', categories=categories)

@bp.route('/delete_post/<int:id>', methods=['POST'])
@login_required
def delete_post(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted successfully.", "success")
    else:
        flash("There is no post with this id.", "error")
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id)
    categories = Category.query.all()
    if request.method == 'POST':
        post.title = request.form['title']
        content = request.form['content']
        post.content = fix_image_src(content)
        selected_categories = request.form.getlist('categories')
        post.categories = Category.query.filter(Category.id.in_(selected_categories)).all()
        db.session.commit()
        flash("Gönderi başarıyla güncellendi!", "success")
        return redirect(url_for('admin.admin_dashboard'))
    
    return render_template('post_form.html', post=post, button_text="Güncelle", categories=categories)

@bp.route('/upload_image', methods=['POST'])
@login_required
def upload_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file extension'}), 400

        filename = secure_filename(file.filename)
        filename = f"{int(time.time())}_{filename}"

        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        if not is_image(filepath):
            os.remove(filepath)
            return jsonify({'error': 'Invalid file type'}), 400

        file_url = url_for('static', filename=f'uploads/{filename}')
        return jsonify({'location': file_url}), 200

    except Exception as e:
        current_app.logger.error(f"Upload error: {str(e)}", exc_info=True)
        return jsonify({'error': f'Upload failed: {str(e)}'}), 500

@bp.route('/restore_backup', methods=['POST'])
@login_required
def restore_backup():
    backup_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../..", "backup_posts.csv")
    
    if not os.path.exists(backup_file):
        flash("Backup dosyası bulunamadı.", "error")
        return redirect(url_for('admin.admin_dashboard'))
    
    df = pd.read_csv(backup_file)

    for _, row in df.iterrows():
        post = Post.query.get(row['id'])
        if post:
            post.title = row['title']
            post.content = row['content']
            post.created_at = row['created_at']
        else:
            new_post = Post(
                id=row['id'],
                title=row['title'],
                content=row['content'],
                created_at=row['created_at']
            )
            db.session.add(new_post)
    db.session.commit()
    
    flash("Veriler backup CSV'den geri yüklendi.", "success")
    return redirect(url_for('admin.admin_dashboard'))