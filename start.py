from flask import Flask
from github_api_covid_data.flask_service.query_service import query_service


def create_app():
    app = Flask(__name__)
    app.register_blueprint(query_service)
    return app


app = create_app()




