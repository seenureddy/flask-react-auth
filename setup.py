import os
import pathlib
import pkg_resources

from setuptools import setup


VERSION_NUMBER = '0.0.1'
# version = VERSION_NUMBER

with open('README.md') as f:
    readme = f.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

print(install_requires)

setup(
    name="flask-react-auth",
    version=VERSION_NUMBER,
    author="Seenureddy",
    description="Flask React authentication",
    long_description=readme,
    keywords="",
    url="",
    packages=['flask-react-auth'],
    # package_data={'': ['templates/*']},
    # include_package_data=True,
    install_requires=install_requires,
    # test_suite='tests',
    # entry_points={'console_scripts': [
    #     'start_ncl = .main:main',
    # ]
    # }
)
