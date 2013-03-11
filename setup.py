"""
Flask-Bowler
--------------

Scripts for Flask-Script to integrate with Twitter Bower

Links
`````
* `Twitter Bower <http://twitter.github.com/bower/>
* `documentation <http://flask-script.readthedocs.org>`_


"""
import sys
from setuptools import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# https://github.com/pypa/virtualenv/pull/259)
try:
    import multiprocessing
except ImportError:
    pass

install_requires = ['Flask-Script']
if sys.version_info < (2, 7):
    install_requires += ['argparse']

setup(
    name='Flask-Bowler',
    version='0.0.1-dev',
    url='http://github.com/holyslon/flask_bower',
    license='BSD',
    author='Anton Onikiichuk',
    author_email='anton@onikiychuk.com',
    description='Add Twitter Bower integration with Flask-Script',
    long_description=__doc__,
    packages=[
        'flask_bower'
    ],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose',
        'mock'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)