from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Harshil Rami"
DESRCIPTION = "This is a first FSDS Nov batch Machine Learning Project"

REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """

    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    requirement_list = []
    file = open(REQUIREMENT_FILE_NAME)
    lines = file.readlines()
    for line in lines:
        requirement_list.append(line.replace("\x00", "").replace("\x00\n", "").replace("ÿþ", ""))

    return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
