from flask import Blueprint, request, render_template
from app.models import ChatHistory

journal_bp = Blueprint('journal', __name__)

# Route to show all journal entries
@journal_bp.route('/journal', methods=['GET'])
def view_journal():
    entries = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).all()
    return render_template('journal.html', entries=entries)

# Route to add a journal entry (just a placeholder for now)
@journal_bp.route('/journal/add', methods=['GET', 'POST'])
def add_journal_entry():
    if request.method == 'POST':
        # TODO: Add your logic to handle POST journal data
        return "Journal entry submitted!"
    else:
        return "This is the journal entry form (GET method)"
