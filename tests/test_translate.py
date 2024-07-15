import unittest
from models.translate import translate_text

class TestTranslation(unittest.TestCase):

    def test_translation_en_to_id(self):
        result = translate_text("Hello", "en", "id")
        self.assertEqual(result, "Halo")

    def test_translation_id_to_en(self):
        result = translate_text("Selamat pagi", "id", "en")
        self.assertEqual(result, "Good morning")

    def test_translation_en_to_fr(self):
        result = translate_text("Hello", "en", "fr")
        self.assertEqual(result, "Bonjour")

    def test_translation_fr_to_en(self):
        result = translate_text("Bonjour", "fr", "en")
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
