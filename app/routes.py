from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from models.translate import translate_text


main = Blueprint('main', __name__)

def get_username_from_token():
    jwt_token = request.cookies.get('jwt_token')
    if jwt_token:
        try:
            decoded_token = decode_token(jwt_token)
            user_id = decoded_token.get('sub')
            user = User.query.filter_by(id=user_id).first()
            if user:
                return user.username
        except Exception as e:
            print(f"Token decoding error: {e}")
            return None
    return None

@main.route('/')
def index():
    username = get_username_from_token()
    return render_template('index.html', username=username)

@main.route('/about')
def about():
    username = get_username_from_token()
    return render_template('about/about.html', username=username)

@main.route('/profile')
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first_or_404()
    user_data = {
        'username': user.username,
        'email': user.email
    }
    return render_template('profile/profile.html', user=user_data)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.form['username']
            password = request.form['password']

        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            response = make_response(jsonify({'access_token': access_token}), 200)
            response.set_cookie('jwt_token', access_token, httponly=True)
            return response  # Returns JSON response for AJAX call
        else:
            return jsonify({'msg': 'Invalid username or password'}), 401

    return render_template('auth/login.html')  # Returns login page for GET request

@main.route('/logout')
def logout():
    response = make_response(redirect(url_for('main.index')))
    response.delete_cookie('jwt_token')
    return response

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists!'}), 400

        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password_hash)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully!', 'user': username}), 201

    return render_template('auth/register.html')


@main.route('/translate', methods=['POST'])
@jwt_required()
def translate():
    current_user = get_jwt_identity()
    data = request.get_json()
    text_to_translate = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')

    if not text_to_translate:
        return jsonify({"msg": "Text to translate is required."}), 400

    translated_text = translate_text(text_to_translate, source_lang, target_lang)

    if translated_text == "Translation model not available.":
        return jsonify({"msg": translated_text}), 400

    return jsonify({"translated_text": translated_text}), 200
