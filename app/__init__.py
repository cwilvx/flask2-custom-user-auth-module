from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import config_options
from . import auth

api = Api()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    api.init_app(app)
    jwt.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


api.add_resource(auth.views.Index, '/')
api.add_resource(auth.views.RegisterUser, '/register')
api.add_resource(auth.views.LoginUser, '/login')
api.add_resource(auth.views.RefreshToken, '/refresh')
