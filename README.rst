==================
Django-epfl-utils
==================

.. image:: https://travis-ci.org/GregLeBarbar/django-epfl-utils.svg?branch=master
    :target: https://travis-ci.org/GregLeBarbar/django-epfl-utils

.. image:: https://coveralls.io/repos/github/GregLeBarbar/django-epfl-utils/badge.svg?branch=master
    :target: https://coveralls.io/github/GregLeBarbar/django-epfl-utils?branch=master

.. image:: https://img.shields.io/pypi/pyversions/django-epfl-utils.svg

.. image:: https://img.shields.io/badge/python-2.7-green.svg

.. image:: https://img.shields.io/badge/django-1.8+-green.svg





Django-epfl-utils is a simple Django app to provide tools common to several 
applications at EPFL.


Install and configure memcached 
***********************************

After installing Memcached itself, you’ll need to install a Memcached binding.
We use python-memcached third party.

CACHES = {
...
    'memcached': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
...
}
