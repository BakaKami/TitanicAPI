import pickle
import sys
import traceback

import pandas as pd

from helper.JSONHelper import JSONHelper
from model.PassangerModel import PassangerModel
from model.SurvivalPredictionViewModel import SurvivalPredictionViewModel


class PassangerService:
    def predict_user_survivability(self, req: PassangerModel) -> SurvivalPredictionViewModel:
        try:
            model_input: dict = {
                "pclass": -1,
                "sex": -1,
                "fare": -1,
                "cabin": -1,
                "boat": -1,
                "body": -1
            }

            if req.pclass is None or req.pclass < 1 or req.pclass > 3:
                raise ValueError("Passanger class must be between 1 and 3")

            model_input["pclass"] = req.pclass or -1

            model_input["sex"] = self.encode_data("sex", req.sex)

            if model_input["sex"] == -1:
                raise ValueError("Sex can only filled by male or female")

            model_input["fare"] = req.fare or -1

            if model_input["fare"] == -1:
                raise ValueError("Fare cannot be empty")

            model_input["cabin"] = self.encode_data("cabin", req.cabin)

            if model_input["cabin"] == -1:
                raise ValueError("Cabin is not registered")

            model_input["boat"] = self.encode_data("boat", req.boat)
            model_input["body"] = req.body or -1

            ml_model = pickle.load(open("model-new.pkl", "rb"))
            df = pd.DataFrame([model_input])

            y_pred = ml_model.predict(df)

            if y_pred == 0:
                return SurvivalPredictionViewModel("Not survived.")

            return SurvivalPredictionViewModel("Survived.")
        except ValueError as e:
            print(traceback.print_exc(), file=sys.stderr)
            return SurvivalPredictionViewModel(error_message=e.args[0], http_code=400)
        except Exception as e:
            print(traceback.print_exc(), file=sys.stderr)
            return SurvivalPredictionViewModel(error_message="Shit happened.", http_code=500)

    def encode_data(self, label: str, original_data: str) -> int:
        if original_data is None:
            return -1

        for data in list(JSONHelper().read_json_from_file(label + "_enc")):
            for item in data.values():
                if item == original_data:
                    return data[label + "_cat"]

        return -1
