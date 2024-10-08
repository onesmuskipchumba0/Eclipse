from setuptools import setup, find_packages

setup(
    name='eclipse',
    version='0.0.01',
    packages=find_packages(),
    install_requires = [
        'rich',
        'pyfiglet'
    ]
)