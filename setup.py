#!/usr/bin/env python3
"""
@author: Ashish Singh
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DeepMRSeg",
    version="0.1.0",
    author="Jimit Doshi",
    author_email="software@cbica.upenn.edu",
    description="Deep Learning based MR image Segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CBICA/DeepMRSeg",
    packages=setuptools.find_packages(),
	install_requires=[
	'tensorflow',
	'tensorflow-addons',
	'dill', 
	'h5py', 
	'hyperopt', 
	'keras',
	'pandas', 
	'protobuf',
	'pymongo',
	'scikit-learn',
	'seaborn',
	'numpy',
	'scipy', 
	'nibabel',
	'subprocess',
	'getopt',
	'signal',
	'time',
	'sys',
	'os',
	'csv',
	'resource',
	'shutil'
	]
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

