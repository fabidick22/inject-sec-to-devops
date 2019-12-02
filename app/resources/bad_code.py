from flask_restful import Resource
from flask.app import Response


class Hello(Resource):
    def get(self):
        return {"message": "hello world from flask!"}, 200


class Base(Resource):
    def get(self):
        return Response("<h3>The API is running..</h3>", mimetype="text/html")

