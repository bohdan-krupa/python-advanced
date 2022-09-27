from setuptools import setup

setup(
    name='text-analyzer',
    version='1.0',
    description='Module for text analazing',
    author='Bohdan Krupa',
    author_email='bodya.save.dev@gmail.com',
    url='',
    packages=['text_analyzer'],
    install_requires=['requests', 'sqlalchemy', 'psycopg2', 'python-dotenv'],
)
