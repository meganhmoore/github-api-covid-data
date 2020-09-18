import os
from github_api_covid_data.lib.gitclass import GitClass


def get_git_user():
    return os.getenv('GIT_USER')


def get_git_pass():
    return os.getenv('GIT_PASS')


def get_credentials():
    user = get_git_user()
    git_pass = get_git_pass()
    if (user is None) or (git_pass is None):
        return None, None
    else:
        return user, git_pass


def get_own_repo():
    """This could be turned into a route to get the specific user's account and either pull a specific repo or create
    one for this project"""
    own_repo = GitClass(name='self', url='https://github.com/meganhmoore/github-api-covid-data', owner='meganhmoore',
                        repo='github-api-covid-data', branch='develop/new_data')
    return own_repo


