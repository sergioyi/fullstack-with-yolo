import os
from flask import Flask
from . import auth
from . import yolo
from flaskr.db import db
from flaskr.user import Users
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SECRET_KEY"] = 'my_secret_key_anonymos'
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(yolo.bp)
    CORS(app, origins="*")
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def apifuncionando():
        return "A aplicação está em funcionamento 🤲"



    if __name__ == '__main__':
        app.run(debug=True)

    return app
