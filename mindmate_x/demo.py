# reset_db.py
from app import create_app, db

app = create_app()

with app.app_context():
    db.drop_all()         # 🔥 Drops all existing tables
    db.create_all()       # 📦 Recreates all tables from models
    print("✅ Database reset successful")
