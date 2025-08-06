from datetime import datetime
from . import db  # Relative import works because `db` is defined in __init__.py

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text)
    ai_reply = db.Column(db.Text)
    mood = db.Column(db.String(20))  # ✅ This line is important
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
