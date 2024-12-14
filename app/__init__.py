from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config  

# Instanciando o banco de dados e o gerenciador de login
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login' 

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.controllers.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.controllers.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/')

    from app.controllers.chat import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/chat')

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User  
    return User.query.get(int(user_id))