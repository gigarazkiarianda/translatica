from flask import Blueprint, render_template, request, jsonify
from models.translate import translate_text 

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/translate', methods=['POST'])
def translate():
    data = request.json 
    text = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')
    translated_text = translate_text(text, source_lang, target_lang)
    return jsonify({'translated_text': translated_text})