# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from js_counters import __version__

setup(
    name='js-counters',
    version=__version__,
    description=open('README.rst').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=['django-filer>=0.9.9','djangocms-icon'],
    include_package_data=True,
    zip_safe=False,
)
