from flask import Flask, Blueprint
from flask_restful import Api
from app.resources.bad_code import Hello, Base, Calc

app = Flask(__name__, instance_relative_config=True)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routing
api.add_resource(Hello, "/hello/", endpoint="hi_ep")
api.add_resource(Calc, "/sum/", endpoint="sum_ep")
api.add_resource(Base, "/", endpoint="base_ep")

app.register_blueprint(api_bp)

