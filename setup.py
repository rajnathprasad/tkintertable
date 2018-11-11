from setuptools import setup
import sys,os
home=os.path.expanduser('~')

setup(
    name = 'tkintertable',
    version = '1.3',
    description = 'Extendable table class for Tkinter',
    url='https://github.com/dmnfarrell/tkintertable',
    license='GPL v3',
    author = 'Damien Farrell',
    author_email = 'farrell.damien[at]gmail.com',
    packages = ['tkintertable'],
    install_requires=['Pmw','future'],
    dependency_links = [
          "http://download.sourceforge.net/pmw/Pmw.1.3.tar.gz"],
    entry_points = { 'gui_scripts': [
                     'tablesapp = tkintertable.App:main']},
    classifiers = ["Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: User Interfaces",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research"],
    keywords = ['tkinter', 'spreadsheet', 'table'],
)
