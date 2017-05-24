#!/usr/bin/env python


from setuptools import setup

setup(
    name='sgol',
    version='0.0.1',
    install_requires=[],
    author='Spatial Current Developers',
    author_email='opensource@spatialcurrent.io',
    license='BSD License',
    url='https://github.com/spatialcurrent/sgol-python/',
    keywords='python',
    description='A Python library for SGOL (Spatial Graph Operations Language).',
    long_description=open('README.rst').read(),
    download_url="https://github.com/spatialcurrent/sgol-python/zipball/master",
    packages=["sgol"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
