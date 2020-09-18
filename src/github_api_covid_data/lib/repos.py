from github_api_covid_data.lib.gitclass import GitClass

# github open datasets
github = GitClass(name='github_covid_data', url='https://github.com/datasets/covid-19', owner='datasets',
                  repo='covid-19', files=['data'])

# Johns Hopkins compilation of daily reported cases and deaths
hopkins = GitClass(name='hopkins_covid_data', url='https://github.com/CSSEGISandData/COVID-19', owner='CSSEGISandData',
                   repo='COVID-19', files=['csse_covid_19_data/csse_covid_19_daily_reports_us',
                                           'csse_covid_19_data/csse_covid_19_daily_reports',
                                           'csse_covid_19_data/csse_covid_19_time_series'])

# NYTimes data also includes cases, deaths (confirmed & probable) as well as
# mask-use data and excess death counts
nytimes = GitClass(name='nytimes_covid_data', url='https://github.com/nytimes/covid-19-data', owner='nytimes',
                   repo='covid-19-data', files=['', 'excess-deaths', 'live', 'mask-use'])

# Our World In Data (Note: might handle diff because not in root of repo)
owid = GitClass(name='owid_covid_data', url='https://github.com/owid/covid-19-data/tree/master/public/data',
                owner='owid', repo='covid-19-data', files=['public/data', 'public/data/ecdc', 'public/data/bsg'])

