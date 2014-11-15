from setuptools import setup

requires = open('requirements.txt').read().split()

entry_points = {
    'console_scripts' : ['ospurge = ospurge.ospurge:main']
}

README = open('README.md').read()

setup(
    name = 'ospurge',
    version = '1.0.0',
    description = 'OpenStack resources cleanup script',
    long_description = README,
    keywords = 'openstack',
    author = 'Florent Flament',
    author_email = 'florent.flament@cloudwatt.com',
    url = 'https://github.com/stackforge/ospurge',
    license = 'MIT',
    packages = ['ospurge'],
    install_requires = requires,
    entry_points = entry_points
)
