"""Creating a singleton so if the user wants to add attributes to a repo (file paths with data or something else) then
they can add it and that information will be captured for the duration of the docker container's life (if they don't
update the repos.py file themselves)"""

class RepoSingleton(object):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            from github_api_covid_data.lib.repos import github, hopkins, nytimes, owid
            cls._instance = cls.__new__(cls)
            cls.repos = [github, hopkins, nytimes, owid]
            cls.repo_map = {f'{github.name}': github, f'{hopkins.name}': hopkins,
            f'{nytimes.name}': nytimes, f'{owid.name}': owid}
        return cls._instance

    def __init__(self):
        raise RuntimeError("Call get_instance instead")

