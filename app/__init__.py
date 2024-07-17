from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:123@localhost/translatica')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        # Impor model di sini untuk menghindari impor melingkar
        from .models.user import User
        db.create_all()

    return app
