from flask import Blueprint, request, jsonify, render_template
from app.services.chatbot_engine import get_ai_reply
from app.models import ChatHistory
from app import db

chatbot_bp = Blueprint('chatbot', __name__)

# POST API: /chat
@chatbot_bp.route('/chat', methods=['POST'])
def handle_chat():
    data = request.get_json()
    user_input = data.get("message", "")

    ai_reply = get_ai_reply(user_input)

    # Save to DB
    chat_log = ChatHistory(user_message=user_input, ai_reply=ai_reply)
    db.session.add(chat_log)
    db.session.commit()

    return jsonify({"reply": ai_reply})

# GET UI: /chatbot
@chatbot_bp.route('/chatbot', methods=['GET'])
def chatbot_ui():
    return render_template('chatbot.html')
