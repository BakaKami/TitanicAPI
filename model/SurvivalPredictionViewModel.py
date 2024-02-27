from model.ErrorViewModel import ErrorViewModel


class SurvivalPredictionViewModel(ErrorViewModel):
    def __init__(self, prediction: str = None, error_message: str = "Success.", http_code: int = 200):
        super().__init__(error_message, http_code)
        if prediction is not None:
            self.prediction = prediction
