from django.core.urlresolvers import reverse
from django.test import RequestFactory, TestCase

from .. import views


class ProjectViewTests(TestCase):
    fixtures = ['projects.json']

    def test_project_list(self):
        """
        ProjectList view shows only projects with public status.

        """
        resp = self.client.get(
            reverse('projects_project_list')
        )
        self.assertEqual(200, resp.status_code)
        self.assertEqual(
            2, len(resp.context['object_list'])
        )
        self.assertEqual(
            ['Test Project 1', 'Test Project 2'],
            [p.name for p in resp.context['object_list']]
        )


class VersionViewTests(TestCase):
    fixtures = ['projects.json']

    def test_version_detail(self):
        url = reverse(
            'projects_version_detail',
            kwargs={
                'project_slug': 'test-project-1',
                'slug': '1.4'}
        )
        resp = self.client.get(url)
        self.assertEqual(200, resp.status_code)
        version = resp.context['object']
        self.assertEqual('1.4', version.version)
        self.assertEqual(
            'test-project-1',
            version.project.slug
        )

    def test_version_detail_non_public(self):
        url = reverse(
            'projects_version_detail',
            kwargs={
                'project_slug': 'test-project-3',
                'slug': '1.0'}
        )
        resp = self.client.get(url)
        self.assertEqual(404, resp.status_code)

    def test_latest_versions(self):
        expected = [
            ('test-project-1', '1.4'),
            ('test-project-2', '22.6'),
        ]
        resp = self.client.get(
            reverse('projects_latest_versions')
        )
        self.assertEqual(200, resp.status_code)
        version_list = resp.context['object_list']
        self.assertEqual(2, len(version_list))
        for version in version_list:
            self.assertTrue(
                (version.project.slug, version.version) in
                expected
            )

    def test_version_detail_no_kwarg(self):
        factory = RequestFactory()
        request = factory.get('/projects/1.4/')
        self.assertRaises(
            AttributeError,
            views.VersionDetail.as_view(),
            request=request, slug='1.4')
