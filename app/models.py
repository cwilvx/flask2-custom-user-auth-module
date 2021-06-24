import bson
import pymongo
from bson import ObjectId
from passlib.hash import bcrypt_sha256 as sha256


class Mongo:
    def __init__(self, database):
        mongo_uri = "mongodb://127.0.0.1:27017/"
        self.db = pymongo.MongoClient(mongo_uri)[database]


class Users(Mongo):
    def __init__(self):
        super(Users, self).__init__('users0')
        self.db = self.db['all_users']

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed_password):
        return sha256.verify(password, hashed_password)

    def register_user(self, user_details):
        self.db.insert_one(user_details)

    def get_user_by_username(self, username):
        user = self.db.find_one({"username": username})
        return user

    def get_all_users(self):
        users = self.db.find()
        return users

    def get_user_by_id(self, user_id):
        try:
            user = self.db.find_one({'_id': ObjectId(user_id)})
        except bson.errors.InvalidId:
            user = {'message': 'Invalid Id'}

        return user
