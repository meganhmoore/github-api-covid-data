from typing import Optional
import requests

from github_api_covid_data.lib.utils import get_credentials
from github_api_covid_data.lib.constants import GITHUB_API_URL
from github_api_covid_data.lib.gitclass import GitClass


def get_repo_data(git_class: GitClass):
    """Get any kind of overarching data about the repo"""
    repo_url_pattern = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}'
    # TODO raise error if resp is not a successful returncode
    resp = make_request(repo_url_pattern)
    return dict(resp.headers)


def get_repo_latest(git_class: GitClass) -> str:
    """Get the latest update time from a repo to see if new data has been added"""
    events_url_pattern = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}/events'
    resp = make_request(events_url_pattern)
    status = resp.headers['status']
    if resp.status_code != 200:
        raise ValueError(f"Did not get the event information successfully, got: {status}")
    else:
        return resp.headers['last-modified']


def get_repo_file_contents(git_class: GitClass, parsed: bool = True, filepath: Optional[str] = None):
    """Get the files in a repo and within a given filepath if supplied, will parse just file names or return all github
    information about each file and directory"""
    if filepath:
        file_contents_url_pattern = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}/contents/{filepath}'
        print(f"PATH: {file_contents_url_pattern}")
    else:
        file_contents_url_pattern = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}/contents'
    resp = make_request(file_contents_url_pattern)
    all_data = resp.json()
    if not parsed:
        return all_data
    else:
        parsed_data = []
        for file in all_data:
            parsed_data.append(file['name'])
        return parsed_data


def get_csvs(git_class: GitClass):
    """Get all of the csvs in the filepaths that have been identified as those containing csv data"""
    data = {}
    for file in git_class.files:
        data[file] = []
        csvs_url = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}/contents/{file}'
        resp = make_request(csvs_url).json()
        for resp_file in resp:
            if '.csv' in resp_file['name']:
                data[file].append((resp_file['name']))
    return data


def make_request(url):
    """Generic template to make a get request with credentials"""
    user, git_pass = get_credentials()
    if user is not None:
        resp = requests.get(url, allow_redirects=True, auth=requests.auth.HTTPBasicAuth(user, git_pass))
    else:
        resp = requests.get(url, allow_redirects=True)
    return resp



