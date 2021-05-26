import datetime
import json

from bson import json_util
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

from app.models import Users

user_instance = Users()
user_parser = reqparse.RequestParser()

user_parser.add_argument('username', required=True)
user_parser.add_argument('password', required=True)


class Index(Resource):
    @staticmethod
    def get():
        return {"msg": "This is the base auth route"}


class RegisterUser(Resource):
    @staticmethod
    def post():
        data = user_parser.parse_args()
        username = data['username']
        password = data['password']

        user_details = {
            'username': username,
            'password': user_instance.generate_hash(password),
            'joined_at': datetime.datetime.now()
        }

        try:
            user_instance.register_user(user_details)
            user = json.loads(json.dumps(user_details, default=json_util.default))
            return user, 201
        except:
            return {'msg': "something went wrong"}


class LoginUser(Resource):
    def post(self):
        data = user_parser.parse_args()

        username = data['username']
        unhashed_password = data['password']

        user = user_instance.get_user_by_username(username)
        user_id = user['_id']
        hashed_password = user['password']

        if not user:
            return {'msg': 'User {} does not exist'.format(username)}, 401

        if user_instance.verify_hash(unhashed_password, hashed_password):
            user = {
                'username': username,
                'user_id': str(user_id)
            }

            access_token = create_access_token(user)
            refresh_token = create_refresh_token(user)

            return {
                'msg': 'logged in as {}'.format(username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        else:
            return {'msg': 'wrong username or password'}