from flask import Blueprint, render_template
from app.models import ChatHistory
from collections import Counter
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Fetch all chat entries for the current user
    chats = ChatHistory.query.filter_by(user_id=current_user.id).order_by(ChatHistory.timestamp.asc()).all()

    # Prepare data for charts
    dates = [chat.timestamp.strftime('%Y-%m-%d') for chat in chats]
    moods = [chat.mood for chat in chats if chat.mood]
    mood_counter = Counter(moods)

    return render_template(
        'dashboard.html',
        dates=dates,
        moods=moods,
        mood_data=mood_counter
    )
