from setuptools import setup,find_packages
from typing import List


PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR_NAME = "SACHIN SEN"
DESCRIPTION = "Machine Learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE = "requirements.txt    "

def get_requirements_list()->List[str]:
    
    """
    Description: This function is going to return list of requirement
    mentioned in reuquirements.txt file
    
    returns: This function is goinf to return the list which contain name of 
    libraries mentioned in requirement.txt file 
    """
    
    with open(REQUIREMENT_FILE) as requirement_file:
        return requirement_file.readlines().remove("-e .")


#Declaring variables for setup functions




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
      
    
)

