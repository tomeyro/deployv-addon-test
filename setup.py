# coding: utf-8

import os
import sys

if os.environ.get('USER', '') == 'vagrant':
    del os.link

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

readme = open('README.md').read()
requirements = open('requirements.txt').readlines()
test_requirements = open('test-requirements.txt').readlines()

setup(
    name='deployv-addon-test',
    version='0.9.11',
    description='Test addon for deployv',
    long_description=readme,
    package_data={'': ['templates/files/*', 'templates/*.jinja', 'config/*']},
    author='Tomas Alvarez',
    author_email='tomas@vauxoo.com',
    url='https://github.com/tomeyro/deployv-addon-test',
    download_url='https://github.com/vauxoo/deployv-addon-test',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='vauxootools deployv addon',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=test_requirements,
    entry_points='''
        [console_scripts]
        deployvcmd_addon_test=deployv_addon_test:cli
    ''',
    scripts=[]
)
