from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta_segura')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://usuario:senha@localhost/db_assistente')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

    SESSION_COOKIE_SECURE = True 
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 7 
