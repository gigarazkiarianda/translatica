import os

def generate_secret_key():
    return os.urandom(24).hex()

def generate_jwt_secret_key():
    return os.urandom(24).hex()
