from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='gpapi',
      version="0.1",
      description='A quick python wrapper for the the GimmeProxy API ',
      long_description=readme(),
      author='Eric Fourrier',
      author_email='ericfourrier0@gmail.com',
      license='MIT',
      packages=['gpapi'],
      keywords=['proxies', 'get', 'api'],
      zip_safe=False,
      test_suite='test',
      install_requires=[
          'requests>=2.0']
      )
