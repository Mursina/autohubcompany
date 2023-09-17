# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "autohubcompany"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Flask Shopping Cart API",
    author_email="",
    url="",
    keywords=["Swagger", "Flask Shopping Cart API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['autohubcompany=autohubcompany.__main__:main']},
    long_description="""\
    A Flask application for managing a shopping cart.
    """
)
