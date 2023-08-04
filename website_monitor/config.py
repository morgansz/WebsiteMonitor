import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
