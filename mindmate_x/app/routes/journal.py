from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models import ChatHistory
from app import db

journal_bp = Blueprint('journal', __name__)

# Route to display all journal entries
@journal_bp.route('/journal', methods=['GET'])
def view_journal():
    entries = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).all()
    return render_template('journal.html', entries=entries)

# Optional: Route to manually add journal entries (for testing / future UI)
@journal_bp.route('/journal/add', methods=['GET', 'POST'])
def add_journal_entry():
    if request.method == 'POST':
        user_message = request.form.get('user_message')
        ai_reply = request.form.get('ai_reply')
        mood = request.form.get('mood')

        if user_message and ai_reply:
            entry = ChatHistory(
                user_message=user_message,
                ai_reply=ai_reply,
                mood=mood
            )
            db.session.add(entry)
            db.session.commit()
            flash("Journal entry added successfully!", "success")
            return redirect(url_for('journal.view_journal'))
        else:
            flash("Both message and reply are required.", "danger")
            return redirect(url_for('journal.add_journal_entry'))

    return render_template('add_journal.html')  # <-- optional if you build a form
