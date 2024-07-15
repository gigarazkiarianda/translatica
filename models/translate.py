from transformers import MarianMTModel, MarianTokenizer

# Model names for translation
model_helsinki_dict = {
    'en-id': 'Helsinki-NLP/opus-mt-en-id',
    'id-en': 'Helsinki-NLP/opus-mt-id-en',
    'en-de': 'Helsinki-NLP/opus-mt-en-fr',
    'de-en': 'Helsinki-NLP/opus-mt-fr-en',
    "id-de": "Helsinki-NLP/opus-mt-id-fr",
    'de-id': 'Helsinki-NLP/opus-mt-fr-id',
}

# Load models and tokenizers
models = {name: MarianMTModel.from_pretrained(model) for name, model in model_helsinki_dict.items()}
tokenizers = {name: MarianTokenizer.from_pretrained(model) for name, model in model_helsinki_dict.items()}

def translate_text(text, source_lang, target_lang):
    model_name = f"{source_lang}-{target_lang}"
    
    if model_name not in models:
        return "Translation model not available."

    tokenizer = tokenizers[model_name]
    model = models[model_name]

    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text
