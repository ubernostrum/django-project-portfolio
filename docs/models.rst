.. _models:
.. module:: projects.models


Models for software projects
============================

django-project-portfolio provides three models which work together
to describe software projects: :class:`~Project` represents a software
project, :class:`~Version` represents a particular version of a
project, and :class:`~License` represents the license under which a
particular version is released.


.. class:: License

   The license under which a particular :class:`~Version` is
   released. This is tied to ``Version`` rather than
   :class:`~Project` in order to allow the possibility of relicensing
   from one version to another.

   A ``License`` has three fields, all of which are required:

   .. attribute:: name

      ``CharField(max_length=255)``

      The name of the license (for example, "GPLv2" or
      "MIT").

   .. attribute:: slug

      ``SlugField`` (prepopulated from :attr:`name`)

      A short, descriptive URL-safe string to identify the
      license. Currently there are no views in
      django-project-portfolio which make use of this, but the
      field is provided so that custom views can make use of it.

   .. attribute:: link

      ``URLField``

      A link to an online version of the license's terms, or to a
      description of the license. For open-source licenses, individual
      license pages in `the OSI license list
      <http://opensource.org/licenses>`_ are useful values for this
      field.


.. class:: Project

   A software project.

   Four fields (all required) provide basic metadata about the
   project:

   .. attribute:: name

      ``CharField(max_length=255)``

      The name of the project.

   .. attribute:: slug

      ``SlugField`` (prepopulated from :attr:`name`)

      A short, descriptive URL-safe string to identify the
      project.

   .. attribute:: description

      ``TextField``

      A free-form text description of the project.

   .. attribute:: status

      ``IntegerField`` with choices

      Indicates whether the project is public or not. May be expanded
      to include additional options in future versions, hence the
      implementation as an ``IntegerField`` with choices instead of a
      ``BooleanField``. Valid choices are:

   .. attribute:: PUBLIC_STATUS

      Indicates a project which is public; this will cause built-in
      views to list and display the project.

   .. attribute:: HIDDEN_STATUS

      Indicates a project which is hidden; built-in views will not
      list or display the project.

   Four additional fields, all optional, allow additional useful data
   about the project to be specified:

   .. attribute:: package_link

      ``URLField``

      URL of a location where packages for this project can be found.

   .. attribute:: repository_link

      ``URLField``

      URL of the project's source-code repository.

   .. attribute:: documentation_link

      ``URLField``

      URL of the project's online documentation.

   .. attribute:: tests_link

      ``URLField``

      URL of the project's online testing/continuous integration
      status.

   One utility method is also defined on instances of ``Project``:

   .. method:: latest_version()

      Returns the latest :class:`~Version` of this project (as defined
      by the ``is_latest`` field on ``Version``), or ``None`` if no
      such version exists.

   Finally, the default manager for ``Project`` defines one custom
   query method, ``public()``, which returns only instances whose
   :attr:`status` is :attr:`PUBLIC_STATUS`. This is implemented via a
   custom ``QuerySet`` subclass, so the method will be available on
   any ``QuerySet`` obtained from ``Project`` as well.


.. class:: Version

   A particular version of a software project.

   There are six fields, all of which are required:

   .. attribute:: project

      ``ForeignKey`` to :class:`~Project`

      The project this version corresponds to.

   .. attribute:: version

      ``CharField(max_length=255)``

      A string representing the version's identifier. This is
      deliberately freeform to support different types of versioning
      systems, but be aware that it will (with the built-in views) be
      used in URLs, so URL-safe strings are encouraged here.

   .. attribute:: is_latest

      ``BooleanField``

      Indicates whether this is the latest version of the
      project. When a ``Version`` is saved with ``is_latest=True``, a
      ``post_save`` signal handler will toggle all other versions of
      that :class:`~Project` to ``is_latest=False``.

   .. attribute:: status

      ``IntegerField`` with choices

      The status of this version. Valid choices are (taken from the
      Python Package Index's status choices):

   .. attribute:: PLANNING_STATUS

      This is an early/planning version.

   .. attribute:: PRE_ALPHA_STATUS

      This is a pre-alpha version.

   .. attribute:: ALPHA_STATUS

      This is an alpha version.

   .. attribute:: BETA_STATUS

      This is a beta version.

   .. attribute:: STABLE_STATUS

      This is a stable version.

   .. attribute:: license

      ``ForeignKey`` to :class:`~License`

      The license under which this version is released.

   .. attribute:: release_date

      The date on which this version was released.

   Additionally, the default manager for ``Version`` defines one
   custom query method, ``stable()``, which returns only instances
   whose :attr:`status` is :attr:`STABLE_STATUS`. This is implemented
   via a custom ``QuerySet`` subclass, so the method will be available
   on any ``QuerySet`` obtained from ``Version`` as well, and also on
   any related ``QuerySet`` obtained through an instance of
   :class:`~Project`.