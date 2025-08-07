from flask import Blueprint, request, jsonify, render_template
from app.services.chatbot_engine import get_ai_reply
from app.models import ChatHistory
from app import db
from flask_login import login_required, current_user

chatbot_bp = Blueprint('chatbot', __name__)

# POST API: /chat
@chatbot_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    mood = data.get("mood", "")  # Optional mood input

    ai_reply = get_ai_reply(user_input)

    # Save to DB with mood and user
    chat_log = ChatHistory(
        user_id=current_user.id,  # Link to logged-in user
        user_message=user_input,
        ai_reply=ai_reply,
        mood=mood
    )
    db.session.add(chat_log)
    db.session.commit()

    return jsonify({"reply": ai_reply})

# GET UI: /chatbot (renders chatbot.html page)
@chatbot_bp.route('/chatbot', methods=['GET'])
@login_required
def chatbot_ui():
    return render_template('chatbot.html')
