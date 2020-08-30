from setuptools import (setup, find_packages)

from drs_client import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='drs_client',
    version=__version__,
    author='ELIXIR Cloud & AAI',
    author_email='sarthakgupta072@gmail.com',
    description='GA4GH DRS Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url='https://github.com/elixir-cloud-aai/DRS-cli.git',
    packages=find_packages(),
    keywords=(
        'ga4gh drs elixir rest restful api app server python'
    ),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[],
    python_requires='>=3.7'
)