from flask import Flask

from route.PassangerRoutes import passanger_api

app = Flask(__name__)
app.register_blueprint(passanger_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
