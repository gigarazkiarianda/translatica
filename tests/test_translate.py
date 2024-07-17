import unittest
from app import create_app, db
from app.models.user import User

class TranslateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password_confirmed': 'password123'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'password_confirmed': 'password123'
        })
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
