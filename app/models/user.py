# app/models/user.py
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    user_email = db.Column(db.String(100), unique=True, nullable=False)
    user_password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.user_name}>'
