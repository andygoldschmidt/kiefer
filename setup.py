import pypandoc
from setuptools import setup


requirements = ['requests-oauthlib==0.5.0', ]

long_description = open('README.rst').read()

setup(
    name='kiefer',
    version='0.1.2b',
    description='A Python wrapper for the Jawbone UP API.',
    long_description=long_description,
    author='Andy Goldschmidt',
    author_email='andy@abby.io',
    license='MIT',
    url='https://github.com/andygoldschmidt/kiefer',
    install_requires=requirements
)
