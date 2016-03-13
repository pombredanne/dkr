from setuptools import setup

setup(name='dkr',
      version='0.1.0',
      description='A python tool to manage multiple docker repos',
      url='https://github.com/beniji/dkr',
      author='beniji',
      license='Apache Licence 2.0',
      packages=['docker_manager'],
      install_requires=['requests==2.2.1'],
      scripts=['bin/dkr'],
      zip_safe=False)
