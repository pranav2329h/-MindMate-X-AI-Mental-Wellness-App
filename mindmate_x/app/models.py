from datetime import datetime
from flask_login import UserMixin
from app import db  # ✅ Correctly import the shared SQLAlchemy instance

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text)
    ai_reply = db.Column(db.Text)
    mood = db.Column(db.String(20))  # Optional: mood tracking
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

class MoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('moods', lazy=True))
