from flask import request, Response
from flask_restful import Resource

from helper.JSONHelper import JSONHelper
from model.PassangerModel import PassangerModel
from model.SurvivalPredictionViewModel import SurvivalPredictionViewModel
from service.PassangerService import PassangerService


class PassangerSurvivalPrediction(Resource):
    def post(self):
        try:
            inputs = PassangerModel(request.json["pclass"], request.json["sex"], request.json["fare"],
                                    request.json["cabin"],
                                    request.json["boat_id"], request.json["body_id"])

            output = PassangerService().predict_user_survivability(inputs)

            return Response(JSONHelper().to_json(output), status=output.http_code, mimetype="application/json")
        except Exception as e:
            return Response(
                JSONHelper().to_json(SurvivalPredictionViewModel(error_message="Shit happened", http_code=500)),
                status=500, mimetype="application/json")
