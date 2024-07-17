from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.key_generator import generate_secret_key, generate_jwt_secret_key
from .. import db  # Gunakan impor relatif

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    secret_key = db.Column(db.String(64), nullable=False)
    jwt_secret_key = db.Column(db.String(64), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.secret_key = generate_secret_key()
        self.jwt_secret_key = generate_jwt_secret_key()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
