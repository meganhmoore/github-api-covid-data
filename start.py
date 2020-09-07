from flask import Flask
from github_api_covid_data.flask_service.query_service import query_service
from github_api_covid_data.flask_service.update_service import update_service


def create_app():
    app = Flask(__name__)
    app.register_blueprint(query_service)
    app.register_blueprint(update_service)
    return app


app = create_app()




