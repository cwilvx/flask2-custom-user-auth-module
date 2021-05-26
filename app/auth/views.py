import datetime
import json

from bson import json_util
from flask_restful import Resource, reqparse

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

        # try:
        user_instance.register_user(user_details)
        user = json.loads(json.dumps(user_details, default=json_util.default))
        return user, 201
        # except:
        #     return {'msg': "something went wrong"}
