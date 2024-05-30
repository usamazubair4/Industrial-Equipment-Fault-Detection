from setuptools import find_packages, setup
from typing import List

Hyphon_dot_E = '-e .'
def get_requirement(file_path:str)-> List[str]:
    '''This function will give the list of requirement packages'''
    requirement = []
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement =[req.replace('\n','') for req in requirement]
        if Hyphon_dot_E in requirement:
            requirement.remove(Hyphon_dot_E)

        return requirement
setup(
    name = 'mlproject',
    version= '0.0.1',
    author= 'usamazubair',
    author_email='usamazubair4@gmail.com',
    packages= find_packages(),
    install_requires = get_requirement('requirements.txt')
)