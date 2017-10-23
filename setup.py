import os

from setuptools import setup


setup(name='django-project-portfolio',
      version='1.3.1',
      zip_safe=False,  # eggs are the devil.
      description='A Django application for listing your software projects.',
      long_description=open(os.path.join(os.path.dirname(__file__),
                                         'README.rst')).read(),
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/django-project-portfolio',
      packages=['projects', 'projects.tests', 'projects.migrations'],
      include_package_data=True,
      test_suite='projects.runtests.run_tests',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Framework :: Django :: 1.8',
                   'Framework :: Django :: 1.10',
                   'Framework :: Django :: 1.11',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Utilities'],
      install_requires=[
          'Django>=1.8,!=1.9.*',
      ],
)
