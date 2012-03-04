#!/usr/bin/env python
from setuptools import setup
import sys
import platform

VERSION = "3.0" # find a better way to do so.

requires = ['feedgenerator', 'jinja2', 'pygments', 'docutils', 'pytz']
if sys.version_info < (2,7):
    requires.append('argparse')

scripts = ['tools/pelican', 'tools/pelican-themes', 'tools/pelican-import', 'tools/pelican-quickstart']

if sys.platform.startswith('win'):
    scripts += [
        'bin/pelican.bat', 'tools/pelican-themes.bat',
        'tools/pelican-import.bat', 'tools/pelican-quickstart.bat'
    ]

setup(
    name = "pelican",
    version = VERSION,
    url = 'http://alexis.notmyidea.org/pelican/',
    author = 'Alexis Metaireau',
    author_email = 'alexis@notmyidea.org',
    description = "A tool to generate a static blog, with restructured text (or markdown) input files.",
    long_description=open('README.rst').read(),
    packages = ['pelican'],
    include_package_data = True,
    install_requires = requires,
    scripts = scripts,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
)
