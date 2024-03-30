from setuptools import setup

setup(name='oaris',
      version='0.0.1',
      description='RIS package for OpenAlex',
      maintainer='John Kitchin',
      maintainer_email='jkitchin@cmu.edu',
      license='MIT',
      packages=['oaris'],
      entry_points={'console_scripts': ['oaris = oaris.main:main']},
      long_description='''Given a DOI get an RIS entry.''')
