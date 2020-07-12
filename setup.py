from setuptools import setup, find_packages
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


version = '0.0.1'

install_requires = [
    'nmigen @ git+https://github.com/nmigen/nmigen.git',
    'Flask==1.1.2',
    'requests==2.24.0',
]

setup(
    name='nmigen-visualiser',
    version=version,
    description="Use javascript to visualise nMigen simulations in realtime.",
    long_description=README,
    classifiers=[
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: LGPLv3+",
        "Programming Language :: Python :: 3",
    ],
    keywords='nMigen nmigen javascript visualiser visualizer frontend',
    author='Yehowshua Immanuel',
    author_email='yehowshua@systemeslibres.org',
    url='https://github.com/BracketMaster/nmigen_visualiser',
    license='GPLv3+',
    packages=find_packages(exclude=["*.demo*"]),
    package_data={"nmigen_visualiser": ["templates/base.html"],},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
