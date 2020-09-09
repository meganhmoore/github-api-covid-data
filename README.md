# github-api-covid-data

This project uses the GithubAPI to query a range of github repositories that contain data about covid-19. The user in 
mind is a researcher that wants to gather covid data for their own modelling or reporting purposes. They have a range 
of github repos that they are monitoring, and they may want to pull new data, or just investigate what is new in each 
repo. This service provides a range of routes so they can gather data about their sources, updates to the data, and the
data that is available for them to work with. 

## The Tech Stack
This is a python-flask service that is built and deployed in a docker container to allow for scalability and to be able
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
    - If you do not set up credentials remove both ENV lines from the file. The service should still work though it
     might not be able to use the update routes that make updates to the repo and you will only be able to make 
     limited requests to the repos.
4. From the root of the cloned repository run `docker-compose up` to start up the docker containers
    - The container will continue running and logging in this window, if you open a new terminal window you can check 
    that it has successfully started by running `docker ps` and a container called `app_container` should be up and 
    running.
    - you can go to `localhost:5000` and you should see the `Welcome` message
5. You can then begin interacting with the service as desired, follow the below User Instructions to find some 
suggested uses
6. When you want to tear down the container you can either ctrl-c in the window for the running container, or you 
can `docker kill app_container` from another container. Then to clean it up run `docker rm app_container` and 
`docker image rm app_img`


## To Use
Once deployed the service will be running on `localhost:5000`
### Available Routes:
 
 - `/repos`: will show you the availabe repos that contain covid data
 - `/repos/latest_update`: will show you when each repo was last updated (for example, if you want to pull new data 
 from them)
 - `/repo/<repo_name>`: given a specific repo (from the list of repos returned from the `/repos` route, provide all of 
 the gihub API repo details)
 - `/repos/files`: Get the directories and files in the root of each repo
 - `/repo/<repo_name>/full_file_data`: Get the full information about each directory and file in the root of the repo 
 (not just the name)
 - `/repo/<repo_name>/files`: similar to `/repos/files` but just showing the data for a specific repo you are interested 
 in
 - `/repo/<repo_name>/filepath/<filepath>`: view files and directories at all levels of a given repo, allows the user 
 to browse around the repo to investigate its setup
 - `/repo/<repo_name>/csvs`: gather all of the csv files in the repo no matter where they are and if they are nested in 
 a subdirectory
 -`/new_csvs/<repo_name>`: gather all the csvs in a given repo, and make a record of them by making a file and pushing 
 it to the `develop/new_data` branch of this repo (github-api-covid-data) for this date and timestamp with a commit 
 message to indicate which repo you are tracking.
 - `/new_csvs`: gather all the csvs for all repos being tracked, and make a record of them by making a file and pushing 
 it to the `develop/new_data` branch of this repo (github-api-covid-data) for this date and timestamp
 
 
## To Develop
1. If you do not have a conda or miniconda install, you can download one for you operating system following the 
instructions on this website: <https://docs.conda.io/en/latest/miniconda.html#installing>.
2. Create a conda environment by running `conda create -n covidApp python=3.7`
3. Activate: `conda activate covidApp`
4. Install dependencies by running: `python setup.py develop`
5. You can test that everything is installed correctly by running the test suite: `python -m pytest tests/`
6. From there you can start adding features and tests 
 

## Next things I would add (with more time)
1. Allow the user to configure their own repo that they want to push updated covid data
    - This could be a post that creates a new GitClass object (monitored by the singleton object?), that then gets 
    referenced by the update commands instead of defaulting to my own repo
2. Allow the user to add new covid repos that they find and want to add data from
    - similar to the above, but not pushed to 
3. Allow users to update existing repos if they find new information (like new types of data/filepaths that existing 
repos now provide)
    - this is the use for the singleton (more stable if it was a database), which would be used to update and 
    filepaths it should track and other info
4. Following from #3 it would make sense to create a database to track the data we have about each repo, as well as 
being able to load the csv data into there to have it in one shared space.
5. To make it more user-friendly it would be useful to add a GUI with some dropdowns for the different repos and the 
ability to view the csvs and actually build off of that data to visualize some of the different covid data, and how it 
compares between the different reporters (nytimes, hopkins, etc.)