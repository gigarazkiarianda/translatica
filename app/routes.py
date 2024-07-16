from flask import Blueprint, render_template, request, jsonify
from models.translate import translate_text 

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about/about.html')

@main.route('/profile')
def profile():
    user = {
        'username': 'JohnDoe',
        'email': 'john@example.com'
    }
    return render_template('profile/profile.html', user=user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        pass
    return render_template('auth/login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic
        pass
    return render_template('auth/register.html')

@main.route('/translate', methods=['POST'])
def translate():
    data = request.json 
    text = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')
    translated_text = translate_text(text, source_lang, target_lang)
    return jsonify({'translated_text': translated_text})