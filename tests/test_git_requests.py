import os
import pytest
import requests

from github_api_covid_data.lib.constants import GITHUB_API_URL
from github_api_covid_data.lib.get_github_data import get_repo_data, get_repo_latest, get_repo_file_contents
from github_api_covid_data.lib.gitclass import GitClass
from github_api_covid_data.lib.repos import github, hopkins, nytimes, \
    owid


@pytest.fixture
def test_repo():
    GitClass(url='https://github.com/meganhmoore/COVID-19', owner='meganhmoore', repo='COVID-19',
             credentials={'user':'meganhmoore', 'pass': 'blah'})


@pytest.fixture
def git_classes():
    return [github, hopkins, nytimes, owid]


def test_basic_repo_access(git_classes):
    """Test access to repos"""
    for git_class in git_classes:
        data = get_repo_data(git_class)
        assert data['status'] == '200 OK'


def test_events(git_classes):
    for git_class in git_classes:
        date = get_repo_latest(git_class)
        now_url = f'{GITHUB_API_URL}/repos/{git_class.owner}/{git_class.repo}'
        now = requests.get(now_url).headers['date']
        assert now > date


def test_file_contents(git_classes):
    for git_class in git_classes:
        contents = get_repo_file_contents(git_class)
        assert (contents[1] == '.gitignore' or contents[1] == 'README.md')




