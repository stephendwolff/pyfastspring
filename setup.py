#!/usr/bin/env python
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# packages = ['pyfastspring']

requires = [
    'requests>=2.17.1,<3',
]

setup(
    name='fastspring',
    version="0.0.1",
    author='Artlogic Media Limited',
    author_email='support@artlogic.net',
    description='A module for working with the FastSpring orders and subscriptopns API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/stephendwolff/fastspring',
    project_urls={
        "Bug Tracker": "https://github.com/stephendwolff/fastspring/issues",
    },
    # packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'pyfastspring': 'pyfastspring'},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Development Status:: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
