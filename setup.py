from setuptools import setup, find_packages

setup(
    name='dirutility',
    version='0.2.19',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'looptools',
        'databasetools',
        'PySimpleGUI',
    ],
    url='https://github.com/mrstephenneal/dirutility',
    license='MIT License',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='Fixed issue preventing Timer from returning elapsed time.',
    long_description='Utility functions for quickly reading directory contents and refactoring folder structure'
)
