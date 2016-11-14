.. _views:
.. module:: projects.views


Views for software projects
===========================


django-project-portfolio provides four built-in views for
displaying information about software projects. Though not all
possible views of the data are included here, the built-in views
strive to cover the common cases.


.. class:: ProjectDetail

   Subclass of `Django's generic DetailView`_.

   Detail view of a :class:`~projects.models.Project`. Has one
   required argument which must be captured in the URL:

   ``slug``

      The :attr:`~projects.models.Project.slug` of the project.

   By default, this view will only display projects whose
   :attr:`~projects.models.Project.status` is
   :attr:`~projects.models.Project.PUBLIC_STATUS`.


.. class:: ProjectList

   Subclass of `Django's generic ListView`_.

   List of :class:`~projects.models.Project` instances.

   By default, this view will only display projects whose
   :attr:`~projects.models.Project.status` is
   :attr:`~projects.models.Project.PUBLIC_STATUS`.


.. class:: VersionDetail

   Subclass of `Django's generic DetailView`_.

   Detail view of a :class:`~projects.models.Version`. Has two
   required arguments which must be captured in the URL:

   ``project_slug``

      The :attr:`~projects.models.Project.slug` of the
      :class:`~projects.models.Project` with which this ``Version`` is
      associated.

   ``slug``

      The :attr:`~projects.models.Version.version` of the ``Version``.

   By default, only versions associated with a
   :class:`~projects.models.Project` whose
   :attr:`~projects.models.Project.status` is
   :attr:`~projects.models.Project.PUBLIC_STATUS` can be displayed.


.. class:: LatestVersionList

   Subclass of ``django.views.generic.ListView``.

   List of the latest :class:`~projects.models.Version` of each public
   (i.e., :attr:`~projects.models.Project.status` is
   :attr:`~projects.models.Project.PUBLIC_STATUS`)
   :class:`~projects.models.Project`.


.. _Django's generic DetailView: https://docs.djangoproject.com/en/1.8/ref/class-based-views/generic-display/#detailview
.. _Django's generic ListView: https://docs.djangoproject.com/en/1.8/ref/class-based-views/generic-display/#listview