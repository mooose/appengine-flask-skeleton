# basedata_api.py
#

import logging

# [START imports]
from flask_restful import Resource, Api

from main import app

api = Api(app)

# [END create_app]


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/basedata/v1/')
