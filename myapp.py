from unicodedata import name
import requests
from pprint import pprint
import numpy as np

# Github username and variables
username = "nginxinc"
example_repo = "ansible-role-nginx"
repos_list = ['Repositories Name']
commits_list = ['Sha of the commits']
tags_list = ['Tags of the repository']

# Url to request
repos_url = f"https://api.github.com/users/{username}/repos"
tags_url = f"https://api.github.com/repos/{username}/{example_repo}/tags"
commits_url = f"https://api.github.com/repos/{username}/{example_repo}/commits"

# Send get request
repo_response = requests.get(repos_url)
tags_response = requests.get(tags_url)
commits_response = requests.get(commits_url)

# Get the json data
repo_data = repo_response.json()
tags_data = tags_response.json()
commits_data = commits_response.json()

# Get repositories of the user
for repository in repo_data:
    repos_list.append(repository["name"])

# Get the tags of one repository
for tags in tags_data:
    tags_list.append(tags["name"])


# Get the commits of one repository
for commits in commits_data:
    commits_list.append(commits["sha"])    

# Save the data to a csv
np.savetxt('/home/manuel/python/python_test/github.csv', [p for p in zip(repos_list, commits_list, tags_list)], delimiter=',', fmt='%s')