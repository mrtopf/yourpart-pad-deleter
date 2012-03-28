from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='deleter',
      version=version,
      description="YouthPart Etherpad Delete Tool",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='COM.lounge',
      author_email='info@comlounge.net',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "pyyaml",
        "starflyer",
        "pytest",
        "paste",
      ],
      entry_points="""
        [starflyer.config]
        default = deleter.setup:setup
        [paste.app_factory]
        main = starflyer:run
      """,
      )
