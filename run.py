from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from app.extensions import db
        from app.models import User, Category
        from app.utils import create_default_categories, backup_posts
        from werkzeug.security import generate_password_hash
        import os
        
        db.create_all()
        create_default_categories()
        backup_posts()

        if not User.query.filter_by(username=os.getenv("ADMIN_USERNAME")).first():
            admin_user = User(
                username=os.getenv("ADMIN_USERNAME"),
                password=generate_password_hash(os.getenv("ADMIN_PASSWORD"))
            )
            db.session.add(admin_user)
            db.session.commit()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
    #    app.run(host="0.0.0.0", port=port)