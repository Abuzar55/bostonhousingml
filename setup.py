from setuptools import find_packages, setup
from typing import List
constant = '-e .'
def get_requirements(filename: str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    req_list = []
    with open(filename, 'r') as f:
        data = f.read()
        req_list = data.split('\n')

        if constant in req_list:
            req_list.remove(constant)
        return req_list
setup(
name='bostonhousingml',
version = '0.0.1',
author='Abuzar55',
author_email='abuzarmajid592@gmail.com',
packages=find_packages(),
install_reuires = get_requirements('requirements.txt')
)