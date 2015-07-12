# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('link', models.URLField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.IntegerField(default=1, choices=[(0, b'Hidden'), (1, b'Public')])),
                ('description', models.TextField()),
                ('package_link', models.URLField(help_text=b"URL of the project's package(s)", null=True, blank=True)),
                ('repository_link', models.URLField(help_text=b"URL of the project's repostory", null=True, blank=True)),
                ('documentation_link', models.URLField(help_text=b"URL of the project's documentation", null=True, blank=True)),
                ('tests_link', models.URLField(help_text=b"URL of the project's tests/continuous integration", null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=255)),
                ('is_latest', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Planning'), (2, b'Pre-Alpha'), (3, b'Alpha'), (4, b'Beta'), (5, b'Stable')])),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('license', models.ForeignKey(to='projects.License')),
                ('project', models.ForeignKey(related_name='versions', to='projects.Project')),
            ],
            options={
                'ordering': ('project', 'version'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('project', 'version')]),
        ),
    ]
