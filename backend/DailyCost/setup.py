from setuptools import setup

setup(
    name='DailyCost',
    packages=['DailyCost'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful'
    ],
)