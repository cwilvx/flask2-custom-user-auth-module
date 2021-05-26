from flask_restful import Resource


class Index(Resource):
    @staticmethod
    def get():
        return {"msg": "This is the base auth route"}
