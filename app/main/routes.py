from flask import render_template, request, redirect, url_for, flash
import html
from app.main import bp
from app.models import Post, Category, post_categories

@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(per_page=5, page=page)
    return render_template('index.html', posts=posts)

@bp.route('/post/<int:id>')
def show_post(id):
    post = Post.query.get_or_404(id)
    post.content = html.unescape(post.content)
    return render_template('post.html', post=post)

@bp.route('/search')
def search(): 
    query = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    if not query:
        return redirect(url_for('main.index'))
    
    results = Post.query.filter(
        (Post.title.ilike(f'%{query}%')) | (Post.content.ilike(f'%{query}%'))
    ).order_by(Post.created_at.desc()).paginate(per_page=5, page=page, error_out=False)

    if results.total == 0:
        flash("Aramanızla eşleşen sonuç bulunamadı.", "info")
    return render_template("search_results.html", results=results, query=query)

@bp.route('/category/<int:cat_id>')
def post_by_category(cat_id):
    category = Category.query.get_or_404(cat_id)
    page = request.args.get('page', 1, type=int)

    posts = (Post.query
             .join(post_categories)
             .filter(post_categories.c.category_id == cat_id)
             .order_by(Post.created_at.desc())
             .paginate(per_page=5, page=page, error_out=False))
    return render_template("category_posts.html", category=category, posts=posts)

@bp.route('/about')
def about():
    return render_template('hakkimda.html')