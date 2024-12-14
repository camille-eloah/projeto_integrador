from flask import Flask
from app.controllers.auth import auth_bp
from app.controllers.chat import chat_bp
from app.controllers.home import home_bp

def register_routes(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(chat_bp, url_prefix='/chat')
    app.register_blueprint(home_bp)
