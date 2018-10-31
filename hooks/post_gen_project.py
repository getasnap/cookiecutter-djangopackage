"""
Does the following:
# 1. Removes the example project if it isn't going to be used
"""

import os
import shutil

#################################################################################
# GLOBALS                                                                       #
#################################################################################
repo_name = '{{ cookiecutter.repo_name }}'
setup_git = True if '{{ cookiecutter.setup_git_repo }}' == "Yes" else False
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_example_project(project_directory):
    """Removes the taskapp if celery isn't going to be used"""
    # Determine the local_setting_file_location
    location = os.path.join(
        PROJECT_DIRECTORY,
        'example'
    )
    shutil.rmtree(location)

# 1. Removes the example project if it isn't going to be used
if '{{ cookiecutter.create_example_project }}'.lower() == 'n':
    remove_example_project(PROJECT_DIRECTORY)

#################################################################################
# SETUP GITHUB REPO                                                             #
#################################################################################
if setup_git:
    err = os.system('bash src/setup_git_repo.sh {}'.format(repo_name))
    if err: print("Error with GitHub repo setup!")

