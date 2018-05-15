from setuptools import setup, find_packages
import quickedit


setup(name='django-quickedit-ng',
      version=quickedit.__version__,
      description='Quick editing of fields in the django admin',
      author='Giorgos Logiotatidis',
      author_email='giorgos@sealabs.net',
      url='http://github.com/giorgos/django-quickedit-ng',
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: Apache Software License',
          ],)
