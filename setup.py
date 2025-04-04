from setuptools import setup, find_packages

setup(
    name='egonetstats',
    version='0.1.1',
    description='A small package for computing egonet composition statistics',
    author='Eun Cheol Choi',
    author_email='euncheol@usc.edu',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
    ],
    python_requires='>=3.6',
)
