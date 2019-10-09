from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='smlp-drf',
    version='0.1b',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)
