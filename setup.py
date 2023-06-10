from setuptools import setup, find_packages

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
