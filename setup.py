from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        ##In the below statement we have a list comprehension which is used to replace the '\n' in the requirements.txt file with empty string
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(name='MLQuestion1',
      version='0.01',
      author='Saravanesh',
      author_email='saravaneshjb@gmail.com',
      install_requires=get_requirements('requirements.txt'),
      packages=find_packages()
      )
