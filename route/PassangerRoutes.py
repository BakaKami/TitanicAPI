from flask import Blueprint
from flask_restful import Api

from route.PassangerSurvivalPrediction import PassangerSurvivalPrediction

passanger_api = Blueprint("passanger_api", __name__)
api = Api(passanger_api)

api.add_resource(PassangerSurvivalPrediction, "/passangers/survival-pred")
