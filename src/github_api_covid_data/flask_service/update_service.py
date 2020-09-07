from flask import Blueprint

from github_api_covid_data.lib.post_github_data import update_csvs

update_service = Blueprint("update_service", __name__)


@update_service.route('/new_csvs/<repo_name>', methods=['PUT'])
def new_csv_update(repo_name: str):
    """Update local repo with new csv data"""
    resp = update_csvs(repo_name)
    return resp


@update_service.route('/new_csvs', methods=['PUT'])
def new_csv_update_all():
    """Update local repo with new csv data"""
    resp = update_csvs()
    return resp
