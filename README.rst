==================
Django-epfl-utils
==================

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
