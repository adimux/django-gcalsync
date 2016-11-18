from distutils.core import setup
from setuptools import find_packages


setup(
        name = "gcalsync",
        # packages=find_packages(),
        packages=["gcalsync"]
        version = "0.1.0",
        description = "A Django application to sync with GCal.",
        author = "Jonathon Morgan",
        author_email = "jonathon@newknowledge.com",
        url = "https://github.com/gati",
        classifiers = [
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
        ],
        install_requires = [
            'rfc3339==5',
            'django-model-utils==2.0.3', 
            'tzlocal==1.1.1', 
            'celery==3.1.11'
            ]
     )
