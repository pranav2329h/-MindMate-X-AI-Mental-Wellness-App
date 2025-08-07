# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindmate.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # Import models *after* initializing db
    from app.models import User

    # Register Blueprints
    from app.routes.journal import journal_bp
    from app.routes.chatbot import chatbot_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.auth import auth_bp
    from app.routes.home import home_bp

    app.register_blueprint(journal_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
