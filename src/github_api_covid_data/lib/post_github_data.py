import base64
from datetime import datetime
import json
import requests
from typing import Optional

from github_api_covid_data.flask_service.repo_singleton import RepoSingleton
from github_api_covid_data.lib.constants import GITHUB_API_URL
from github_api_covid_data.lib.get_github_data import get_csvs
from github_api_covid_data.lib.utils import get_credentials, get_own_repo


def update_csvs(repo_name: Optional[str] = None):
    """This function retrieves all csv files from the specified directories in the repos we are tracking (can use the
    /repos route to find out which are available) and makes a file in repo for this project to make a record of the
    data available on this date, a snapshot that can then be parsed by researchers to determine what data they may want
    to pull."""
    details = {}
    if repo_name:
        repo = RepoSingleton.get_instance().repo_map[repo_name]
        details[repo_name] = get_csvs(repo)
    else:
        repos = RepoSingleton.get_instance().repos
        for repo in repos:
            details[repo.name] = get_csvs(repo)

    own_repo = get_own_repo()
    repo_names = ", ".join(list(details.keys()))
    message = f'New CSV data on {datetime.now()} for repos: {repo_names}'
    branch = own_repo.branch
    date_and_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    path = f'csv_updates/{date_and_time}.txt'

    post_csv_url_pattern = f'{GITHUB_API_URL}/repos/{own_repo.owner}/{own_repo.repo}/contents/{path}'

    ENCODING = 'utf-8'
    content = base64.b64encode(json.dumps(details).encode())
    payload = {'message': message,
               'content': content.decode(ENCODING),
               'branch': branch}

    user, git_pass = get_credentials()
    resp = requests.put(post_csv_url_pattern, json=payload,
                        auth=requests.auth.HTTPBasicAuth(user, git_pass))
    return resp.json()
