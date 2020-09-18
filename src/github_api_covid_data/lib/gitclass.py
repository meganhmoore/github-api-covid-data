from typing import Dict, List, Optional


class GitClass(object):
    def __init__(self, name: str, url: str, owner: str, repo: str, files: Optional[List[str]] = None,
                 credentials: Optional[Dict] = None, branch: Optional[str] = None):
        self.name = name
        self.url = url
        self.owner = owner
        self.repo = repo
        self.files = files
        self.branch = branch
        if credentials:
            self.has_credentials = True
            self.user_auth = credentials['user']
            self.pass_auth = credentials['pass']
        else:
            self.has_credentials = False

    def to_json(self):
        jsonified = {
            'name': self.name,
            'url': self.url,
            'owner': self.owner,
            'repo': self.repo
        }
        return jsonified

    def add_file(self):
        """add a file to the list so that we can display data"""
