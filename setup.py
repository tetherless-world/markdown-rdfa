#! /usr/bin/env python

from setuptools import setup

setup(
    name='markdown-rdfa',
    version='0.1',
    author='James McCusker',
    author_email='mccusj@cs.rpi.edu',
    description='Python-Markdown extension to add support for semantic data (RDFa).',
    url='https://github.com/tetherless-world/markdown-rdfa',
    py_modules=['mdx_rdfa'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License ',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
