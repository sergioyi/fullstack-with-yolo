from flaskr.db import db
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Campo para o hash da senha
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
