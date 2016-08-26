# coding:utf-8
import os
import epflutils
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-epfl-utils',
    version=epflutils.__version__,
    packages=find_packages(),
    include_package_data=True,
    license="LGPLv3",
    description='A simple Django app to provide tools common to several applications at EPFL.',
    long_description=README,
    url='https://charmier@git.epfl.ch/repo/django-utils-epfl.git',
    author='Charmier Grégory',
    author_email='gregory.charmier@epfl.ch',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
