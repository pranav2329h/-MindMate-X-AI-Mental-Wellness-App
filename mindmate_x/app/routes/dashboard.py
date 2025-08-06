from flask import Blueprint, render_template
from app.models import ChatHistory
from collections import Counter
from datetime import datetime
import json

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    chats = ChatHistory.query.order_by(ChatHistory.timestamp.asc()).all()

    dates = [chat.timestamp.strftime('%Y-%m-%d') for chat in chats]
    moods = [chat.mood for chat in chats if chat.mood]

    mood_counter = Counter(moods)

    return render_template('dashboard.html', dates=dates, moods=moods, mood_data=json.dumps(mood_counter))
