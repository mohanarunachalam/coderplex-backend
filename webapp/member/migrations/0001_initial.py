# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('avatar',
                 models.URLField(blank=True, max_length=100, null=True)),
                ('mobile_number',
                 models.CharField(
                     blank=True, default=None, max_length=20, null=True)),
                ('short_bio',
                 models.CharField(
                     blank=True, default=None, max_length=255, null=True)),
                ('job_status', models.NullBooleanField(default=None)),
                ('company_name',
                 models.CharField(
                     blank=True, default=None, max_length=50, null=True)),
                ('looking_for_job', models.NullBooleanField(default=None)),
                ('github_profile',
                 models.URLField(
                     blank=True, default=None, max_length=75, null=True)),
                ('facebook_profile',
                 models.URLField(
                     blank=True, default=None, max_length=75, null=True)),
                ('twitter_profile',
                 models.URLField(
                     blank=True, default=None, max_length=75, null=True)),
                ('linkedin_profile',
                 models.URLField(
                     blank=True, default=None, max_length=75, null=True)),
                ('codepen_profile',
                 models.URLField(
                     blank=True, default=None, max_length=75, null=True)),
                ('discord_profile',
                 models.CharField(
                     blank=True, default=None, max_length=25, null=True)),
                ('familiar_technologies',
                 models.CharField(
                     blank=True, default=None, max_length=255, null=True)),
                ('interested_technologies',
                 models.CharField(
                     blank=True, default=None, max_length=255, null=True)),
                ('user',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='user',
                     to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
