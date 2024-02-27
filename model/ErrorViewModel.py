class ErrorViewModel:
    def __init__(self, error_message: str, http_code: int):
        self.error_message = error_message
        self.http_code = http_code
