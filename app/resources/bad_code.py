from flask_restful import Resource
from flask.app import Response
from flask import request
from config.development import DevelopmentConfig


class Calc(Resource):
    def get(self):
        return {"message": "Method not supported!"}, 501

    def post(self):
        json_data = request.get_json(True)
        print(json_data)
        value_a = json_data.get("a", None)
        value_b = json_data.get("b", None)
        # return value_a + value_b
        return eval("{} + {}".format(value_a, value_b))


class Hello(Resource):
    def get(self):
        return {"message": "hello world from flask!"}, 200

    def post(self):
        json_data = request.get_json(True)
        str_format = json_data.get("text", None)
        return str_format.format(details=DevelopmentConfig())


class Base(Resource):
    def get(self):
        return Response("<h3>The API is running..</h3>", mimetype="text/html")

