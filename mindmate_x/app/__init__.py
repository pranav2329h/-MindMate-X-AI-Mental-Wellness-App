from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindmate.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    from app.routes.journal import journal_bp
    app.register_blueprint(journal_bp)
    from app.routes.chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp)
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)



    return app
