from setuptools import find_packages, setup
from typing import List

hypen_e = '-e .'

'''
    This function will return the requirements list.
      '''

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Ashwin',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

'''
whenever we use open funct, the '\n' also gets added 
into readlines.  so we replace '\n' with blank using req.replace
'''