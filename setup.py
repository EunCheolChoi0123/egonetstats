from setuptools import setup, find_packages

setup(
    name='egonetstats',
    version='0.1.0',
    description='A small package for computing egonet composition statistics',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
    ],
    python_requires='>=3.6',
)
