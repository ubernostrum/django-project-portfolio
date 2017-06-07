.. _install:


Installation guide
==================

The |version| release of django-project-portfolio supports Django 1.8,
1.10, and 1.11 on the following Python versions (matching the versions
supported by Django itself):

* Django 1.8 supports Python 2.7, 3.3, 3.4, and 3.5.

* Django 1.10 supports Python 2.7, 3.4, and 3.5.

* Django 1.11 supports Python 2.7, 3.4, 3.5, and 3.6

.. important:: **Python 3.2**

   Although Django 1.8 supported Python 3.2 at the time of its
   release, the Python 3.2 series has reached end-of-life, and as a
   result support for Python 3.2 has been dropped from
   django-project-portfolio.

If you do not already have a supported version of Django installed,
installing django-project-portfolio will install the latest release of
Django automatically as a dependency.


Normal installation
-------------------

The preferred method of installing django-project-portfolio is via
``pip``, the standard Python package-installation tool. If you don't
have ``pip``, instructions are available for `how to obtain and
install it <https://pip.pypa.io/en/latest/installing.html>`_. If
you're using Python 2.7.9 or later (for Python 2) or Python 3.4 or
later (for Python 3), ``pip`` came bundled with your installation of
Python.

Once you have ``pip``, type::

    pip install django-project-portfolio


Installing from a source checkout
---------------------------------

If you want to work on django-project-portfolio, you can obtain a
source checkout.

The development repository for django-project-portfolio is at
<https://github.com/ubernostrum/django-project-portfolio>. If you have
`git <http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/django-project-portfolio.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``pip install -e .`` (the
``-e`` flag specifies an "editable" install, allowing you to change
code as you work on django-project-portfolio, and have your changes
picked up automatically).


Configuration and use
---------------------

Once you have Django and django-project-portfolio installed, check out
:ref:`the quick start guide <quickstart>` to see how to get your
contact form up and running.