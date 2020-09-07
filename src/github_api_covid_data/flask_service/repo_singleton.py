class RepoSingleton(object):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            from github_api_covid_data.lib.repos import github, hopkins, nytimes, owid
            cls._instance = cls.__new__(cls)
            cls.repos = [github, hopkins, nytimes, owid]
        return cls._instance

    def __init__(self):
        raise RuntimeError("Call get_instance instead")

