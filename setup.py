from pathlib import Path

from setuptools import setup, find_packages


if __name__ == "__main__":

    base_dir = Path(__file__).parent
    src_dir = base_dir / 'src'

    install_requirements = [
        'requests',
    ]

    test_requirements = [
        'pytest',
    ]

    setup(
        name='github-api-covid-data',
        version='1.0.0',

        description='github querying web app',
        long_description='web app to pull data from a series of github repos containing github data',

        author='Megan Moore',
        author_email='mm7148@uw.edu',

        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        include_package_data=True,

        install_requires=install_requirements,
        tests_require=test_requirements,
        extras_require={
            'test': test_requirements
        },

        entry_points={}
    )