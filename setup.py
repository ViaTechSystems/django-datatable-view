# -*- encoding: utf-8 -*-
"""setup.py: Django django-datatables-view"""

from setuptools import setup, find_packages

setup(name='django-datatable-view',
<<<<<<< HEAD
<<<<<<< HEAD
      version='0.9.0-beta.5',
=======
      version='0.9.0-beta.7',
>>>>>>> 2a49700... Get column value when source is callable
=======
      version='0.9.0-beta.6',
>>>>>>> 0a6542e... Lookup types can be passed as arguments to method 'search'
      description='This package is used in conjunction with the jQuery plugin '
                  '(http://http://datatables.net/), and supports state-saving detection'
                  ' with (http://datatables.net/plug-ins/api).  The package consists of '
                  'a class-based view, and a small collection of utilities for rendering'
                  ' table data from models.',
      author='Tim Valenta',
      author_email='tvalenta@pivotalenergysolutions.com',
      url='https://github.com/pivotal-energy-solutions/django-datatable-view',
      download_url='https://github.com/pivotal-energy-solutions/django-datatable-view/tarball/django-datatable-view-0.9.0-beta.5',
      license='Apache License (2.0)',
      classifiers=[
           'Development Status :: 2 - Pre-Alpha',
           'Environment :: Web Environment',
           'Framework :: Django',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: Apache Software License',
           'Operating System :: OS Independent',
           'Programming Language :: Python',
           'Topic :: Software Development',
      ],
      packages=find_packages(exclude=['tests', 'tests.*']),
      package_data={'datatableview': ['static/js/*.js', 'templates/datatableview/*.html']},
      include_package_data=True,
      install_requires=['django>=1.2', 'python-dateutil>=2.1'],
)
