from flask import Flask
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    from app.extensions import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'admin.admin_login'
    
    CSRFProtect(app)
    
    # Register custom filters
    from app.utils import format_turkish_date, process_post_content
    app.template_filter('format_turkish_date')(format_turkish_date)
    app.template_filter('process_post_content')(process_post_content)
    
    # Context processor
    @app.context_processor
    def inject_categories():
        from app.models import Category
        categories = Category.query.all()
        return dict(all_categories=categories)
    
    # Register blueprints
    from app.main import bp as main_bp
    from app.admin import bp as admin_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app