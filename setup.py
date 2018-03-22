from setuptools import setup, find_packages

setup(
    name='gpg_secrets',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'GitPython',
        'python-dotenv',
        'python-gnupg'
    ]
)
