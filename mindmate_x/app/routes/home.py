# app/routes/home.py

from flask import Blueprint, redirect, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return redirect(url_for('dashboard.dashboard'))  # or 'auth.login' or any route you prefer
