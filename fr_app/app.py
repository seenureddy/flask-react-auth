from flask import Blueprint
from flask_restful import Api

# Add Blueprint to Flask App
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# api.add_resource(Resource, '/swagger')
