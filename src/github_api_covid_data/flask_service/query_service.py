"""The query service can make GET requests to the Git API to provide data about different covid repos"""
from flask import Blueprint

from github_api_covid_data.flask_service.repo_singleton import RepoSingleton
from github_api_covid_data.lib.get_github_data import get_repo_data, get_repo_latest, \
    get_repo_file_contents, get_csvs

query_service = Blueprint("query_service", __name__)


@query_service.route('/')
def hello():
    return ("Hello World!")


@query_service.route('/repos', methods=['GET'])
def get_repos():
    """Get all repos that can be queried"""
    repo_data = []
    repos = RepoSingleton.get_instance().repos
    for repo in repos:
        json = repo.to_json()
        print(json)
        repo_data.append(repo.to_json())
    print(repo_data)
    return {"repos": repo_data}


@query_service.route('/repos/latest_update', methods=['GET'])
def get_repos_latest_update():
    """Return the latest update time from each repo"""
    repo_data = {}
    repos = RepoSingleton.get_instance().repos
    for repo in repos:
        latest = get_repo_latest(repo)
        repo_data[repo.name] = latest
    return repo_data


@query_service.route('/repo/<repo_name>', methods=['GET'])
def get_repo_details(repo_name):
    """Get the detailed information about a specifir repo"""
    details = {}
    repos = RepoSingleton.get_instance().repo_map
    try:
        repo = repos[repo_name]
        details[repo.url] = get_repo_data(repo)
    except KeyError:
        details["error"] = "This is not a valid Repo Name"
    return details


@query_service.route('/repos/files', methods=['GET'])
def get_files_in_repos():
    """Get high level directories for each repo"""
    details = {}
    repos = RepoSingleton.get_instance().repos
    for repo in repos:
        details[repo.name] = get_repo_file_contents(repo)
    return details


@query_service.route('/repo/<repo_name>/full_file_data', methods=['GET'])
def get_all_file_data_in_repo(repo_name: str):
    details = {}
    repos = RepoSingleton.get_instance().repo_map
    try:
        repo = repos[repo_name]
        details[repo_name] = get_repo_file_contents(repo, False)
    except KeyError:
        details["error"] = "This is not a valid Repo Name"
    return details


@query_service.route('/repo/<repo_name>/files', methods=['GET'])
def get_file_data_in_repo(repo_name: str):
    details = {}
    repos = RepoSingleton.get_instance().repo_map
    try:
        repo = repos[repo_name]
        details[repo_name] = get_repo_file_contents(repo)
    except KeyError:
        details["error"] = f"This is not a valid Repo Name: {repo_name}"
    return details


@query_service.route('/repo/<repo_name>/filepath/<path:filepath>', methods=['GET'])
def get_filepath_in_repo(repo_name: str, filepath: str):
    details = {}
    repos = RepoSingleton.get_instance().repo_map
    try:
        repo = repos[repo_name]
        details[repo_name] = get_repo_file_contents(repo, filepath=filepath)
    except KeyError:
        details["error"] = "This is not a valid Repo Name"
    return details


@query_service.route('/repo/<repo_name>/csvs', methods=['GET'])
def get_csvs_in_repo(repo_name: str):
    details = {}
    repos = RepoSingleton.get_instance().repo_map
    try:
        repo = repos[repo_name]
        details[repo_name] = get_csvs(repo)
    except KeyError:
        details["error"] = "This is not a valid Repo Name"
    return details

