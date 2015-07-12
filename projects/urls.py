from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.ProjectList.as_view(),
        name='projects_project_list'),
    # This pattern has to come first, or "versions" will be
    # interpreted as a project slug. As a side effect, this means a
    # custom URLconf is needed in order to have a Project whose slug
    # *is* the string "versions".
    url(r'^versions/$',
        views.LatestVersionsList.as_view(),
        name='projects_latest_versions'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.ProjectDetail.as_view(),
        name='projects_project_detail'),
    url(r'^(?P<project_slug>[-\w]+)/(?P<slug>[\w\d\.-]+)/$',
        views.VersionDetail.as_view(),
        name='projects_version_detail'),
]
