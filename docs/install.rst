.. _install:


Installation guide
==================

Before installing django-project-portfolio, you'll need to have a
copy of `Django <https://www.djangoproject.com>`_ already
installed. For information on obtaining and installing Django, consult
the `Django download page <https://www.djangoproject.com/download/>`_,
which offers convenient packaged downloads and installation
instructions.

The |version| release of django-project-portfolio supports Django 1.8,
1.9, and 1.10, on the following Python versions:

* Django 1.8 suports Python 2.7, 3.3, 3.4 and 3.5.

* Django 1.9 supports Python 2.7, 3.4 and 3.5.

* Django 1.10 supports Python 2.7, 3.4 and 3.5.

It is expected that django-project-portfolio |version| will work
without modification on Python 3.6 once it is released.

.. important:: **Python 3.2**

   Although Django 1.8 supported Python 3.2 at the time of its
   release, the Python 3.2 series has reached end-of-life, and as a
   result support for Python 3.2 has been dropped from
   django-project-portfolio.


Normal installation
-------------------

The preferred method of installing django-project-portfolio is via ``pip``,
the standard Python package-installation tool. If you don't have
``pip``, instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_. If you're using
Python 2.7.9 or later (for Python 2) or Python 3.4 or later (for
Python 3), ``pip`` came bundled with your installation of Python.

Once you have ``pip``, simply type::

    pip install django-project-portfolio


Manual installation
-------------------

It's also possible to install django-project-portfolio
manually. To do so, obtain the latest packaged version from `the
listing on the Python Package Index
<https://pypi.python.org/pypi/django-project-portfolio/>`_. Unpack the
``.tar.gz`` file, and run::

    python setup.py install

Once you've installed django-project-portfolio, you can verify
successful installation by opening a Python interpreter and typing
``import projects``.

If the installation was successful, you'll simply get a fresh Python
prompt. If you instead see an ``ImportError``, check the configuration
of your install tools and your Python import path to ensure
django-project-portfolio installed into a location Python can
import from.


Installing from a source checkout
---------------------------------

The development repository for django-project-portfolio is at
<https://github.com/ubernostrum/django-project-portfolio>. Presuming
you have `git <http://git-scm.com/>`_ installed, you can obtain a copy
of the repository by typing::

    git clone https://github.com/ubernostrum/django-project-portfolio.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``python setup.py install``.


Basic use
---------

You'll need to add django-project-portfolio to your Django-based
project; since this application makes use of a custom signal which
needs to be set up, it's done via `a Django AppConfig
<https://docs.djangoproject.com/en/dev/ref/applications/#configuring-applications>`_
subclass. So rather than adding ``projects`` to your
``INSTALLED_APPS`` setting, instead add
``projects.apps.ProjectsConfig``, like so::

    INSTALLED_APPS = [
        # ... other apps here
       'projects.apps.ProjectsConfig',
    ]

Then run ``manage.py migrate`` to set up the required database tables,
and you can start adding instances of :ref:`the provided models
<models>` though the Django admin interface, and wiring up :ref:`the
provided views <views>` in your URLconf.

