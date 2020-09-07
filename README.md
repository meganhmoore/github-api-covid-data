# github-api-covid-data

This project uses the GithubAPI to query a range of github repositories that contain data about covid-19. The user in 
mind is a researcher that wants to gather covid data for their own modelling or reporting purposes. They have a range 
of github repos that they are monitoring, and they may want to pull new data, or just investigate what is new in each 
repo.

## The Tech Stack
This is a python-flask service that is build and deployed in a docker container to allow for scalability and to be able
to use dependencies in a static space no matter what the underlying machine has. 
1. Python 3.7 is used
2. Flask is the python package for creating web apps: <https://flask.palletsprojects.com/en/1.1.x/>. The user will 
make requests to the Flask routes 
3. The Python Requests package is used to make requests to the Github API to gather data from the chosen repos:
 <https://requests.readthedocs.io/en/master/>.
4. Docker is using a uswgi-nginx docker image built for flask apps, this can be configured to scale with request load 

## To Deploy
1. Clone the Repository: `git clone https://github.com/meganhmoore/github-api-covid-data.git`
2. Download docker for your OS (<https://www.docker.com/products/docker-desktop>) if you do not already have it 
installed, and create a docker account: <https://hub.docker.com/>
3. If you want to use github credentials (see: 
<https://docs.github.com/en/rest/overview/resources-in-the-rest-api#authentication> for instructions), create your 
credentials and paste your username in the Dockerfile where it says <YOUR_GIT_USERNAME> and paste your git access key 
where it says <YOUR_GIT_ACCESS_KEY>.
    - If you do not set up credentials remove both ENV lines from the file. The service should still work, but you will 
    be able to make limited requests to the repos.
4. From the root of the cloned repository run `docker-compose up` to start up the docker containers
    - The container will continue running and logging in this window, if you open a new terminal window you can check 
    that it has successfully started by running `docker ps` and a container called `app_container` should be up and 
    running.
    - you can go to `localhost:5000` and you should see the `Hello World` message
5. You can then begin interacting with the service as desired, follow the below User Instructions to find some 
suggested uses


## To Use
Once deployed the service will be running on `localhost:5000`
### Available Routes:
 
 - `/repos`: will show you the availabe repos that contain covid data
 - `/repos/latest_update`: will show you when each repo was last updated (for example, if you want to pull new data 
 from them)
 - `/repo/<repo_name>`: given a specific repo (from the list of repos returned from the `/repos` route, provide all of 
 the gihub API repo details)
 
 
## To Develop
1. If you do not have a conda or miniconda install, you can download one for you operating system following the 
instructions on this website: <https://docs.conda.io/en/latest/miniconda.html#installing>.
2. Create a conda environment by running `conda create -n covidApp python=3.7`
3. Activate: `conda activate covidApp`
4. Install dependencies by running: `python setup.py develop`
5. You can test that everything is installed correctly by running the test suite: `python -m pytest tests`
6. From there you can start adding features and tests 
 