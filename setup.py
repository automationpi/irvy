from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

setup(
    name='irvy',
    version='0.0.1',
    packages=['irvy', 'irvy.generators'],  # specify packages here
    include_package_data=True,
    install_requires=[
        # list of dependencies
    ],
    entry_points={
        'console_scripts': [
            'irvy=irvy.irvy:main',
        ],
    },
)
