from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-ReactJS',
    version='0.1',
    packages=['flask_react'],
    url='https://github.com/gerelorant/flask_react',
    license='MIT',
    author='Gere Lóránt',
    author_email='gerelorant@gmail.com',
    description='React extension for Flask',
    install_requires=['Flask'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
