from pip.req import parse_requirements
import pypandoc
from setuptools import setup

parsed_reqs = parse_requirements('requirements.txt', session='foo')
requirements = [str(p.req) for p in parsed_reqs]

long_description = open('README.rst').read()

setup(
    name='kiefer',
    version='0.1.1',
    description='A Python wrapper for the Jawbone UP API.',
    long_description=long_description,
    author='Andy Goldschmidt',
    author_email='andy@abby.io',
    license='MIT',
    url='https://github.com/andygoldschmidt/kiefer',
    install_requires=requirements
)
