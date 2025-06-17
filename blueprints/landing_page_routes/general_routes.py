# This routes are initialized in __init__.py which is called from app.py

from flask import Blueprint, render_template

general_bp = Blueprint('general_bp', __name__)

# Landing to main page
@general_bp.route('/')
def index():
    return render_template('landing_page.html')


# Directing to SQL
@general_bp.route('/sql')
def sql_page():
    return render_template('landing_page_directing_to_templates/sql_page.html')


# Directing to statistics
@general_bp.route('/statistics')
def statistics_page():
    return render_template('landing_page_directing_to_templates/statistics_page.html')


# Directing to python
@general_bp.route('/python')
def python_page():
    return render_template('landing_page_directing_to_templates/python_page.html')


# Directing to ML
@general_bp.route('/ml')
def ml_page():
    return render_template('landing_page_directing_to_templates/ml_page.html')


# Directing to DL
@general_bp.route('/dl')
def dl_page():
    return render_template('landing_page_directing_to_templates/dl_page.html')


# Directing to NLP
@general_bp.route('/nlp')
def nlp_page():
    return render_template('landing_page_directing_to_templates/nlp_page.html')


# Directing to LLMs
@general_bp.route('/llm')
def llm_page():
    return render_template('landing_page_directing_to_templates/llm_page.html')
