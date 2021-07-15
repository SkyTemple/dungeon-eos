__version__ = '0.0.1'
import os

from setuptools import setup, find_packages

setup(
  name = 'dungeon-eos', 
  packages = find_packages(),
  version = __version__,
  license='GPL',
  description = 'A package that simulates PMD EoS dungeon generation. ',
  author = 'irdkwia idkmn', 
  author_email = 'irdkwia2000@gmail.com', 
  url = 'https://github.com/irdkwia/dungeon_eos/',
  keywords = ['Dungeon', 'PMD', 'Explorers', 'Generator'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
