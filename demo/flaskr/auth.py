from flask import Blueprint, request, jsonify, session, flash
from flaskr.user import Users
from flaskr.db import db

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/auth/register', methods=['POST'])
def create_user():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password or not email:
            return jsonify({"message": "Todos os campos (username, password, email) são obrigatórios!"}), 400

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "E-mail já cadastrado!"}), 400

        user = Users(username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Usuário criado com sucesso!"}), 201

    except Exception as erro:
        print(f"Erro ao criar usuário: {erro}")
        db.session.rollback()
        return jsonify({"message": "Erro interno no servidor.", "error": str(erro)}), 500



@bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    error = None

    # Verificar se o usuário existe
    user = Users.query.filter_by(username=username).first()

    if user is None:
        error = 'Usuário incorreto.'
    elif not user.check_password(password):
        error = 'Senha incorreta.'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        return jsonify({"message": "Login aprovado", "username": user.username}), 200

    # Retornar o erro em formato JSON
    return jsonify({"message": error}), 400

