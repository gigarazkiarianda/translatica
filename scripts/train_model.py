from transformers import MarianMTModel, MarianTokenizer

def load_and_save_model(model_name, save_path):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)
    print(f"Model and tokenizer for {model_name} saved to {save_path}")

if __name__ == '__main__':
    models = [
        'Helsinki-NLP/opus-mt-en-id',
        'Helsinki-NLP/opus-mt-id-en',
        'Helsinki-NLP/opus-mt-en-fr',
        'Helsinki-NLP/opus-mt-fr-en',
        'Helsinki-NLP/opus-mt-id-fr',
        'Helsinki-NLP/opus-mt-de-id',
    ]
    
    for model_name in models:
        load_and_save_model(model_name, f"./models/{model_name.split('/')[-1]}")
