from setuptools import setup, find_packages

setup(name='personalpackage',
      version='0.1.0',
      description='Personal Package',
      url='',
      author='Jan Caha',
      author_email='',
      license='MIT',
      packages=find_packages(),
      install_requires=['gdal', 'pyproj']
      )
