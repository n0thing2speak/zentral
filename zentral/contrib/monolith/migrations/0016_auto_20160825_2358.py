# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 23:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import zentral.contrib.monolith.models


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0015_manifest_mbu_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubManifestAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(choices=[('managed_installs', 'Managed Installs'), ('managed_uninstalls', 'Managed Uninstalls'), ('optional_installs', 'Optional Installs'), ('managed_updates', 'Managed Updates')], max_length=32)),
                ('type', models.CharField(choices=[('package', 'package'), ('configuration_profile', 'configuration_profile')], max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('identifier', models.TextField()),
                ('version', models.PositiveSmallIntegerField(default=0)),
                ('file', models.FileField(upload_to=zentral.contrib.monolith.models.attachment_path)),
                ('pkg_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed_at', models.DateTimeField(null=True)),
                ('sub_manifest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monolith.SubManifest')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='submanifestconfigurationprofile',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='submanifestconfigurationprofile',
            name='sub_manifest',
        ),
        migrations.DeleteModel(
            name='SubManifestConfigurationProfile',
        ),
        migrations.AlterUniqueTogether(
            name='submanifestattachment',
            unique_together=set([('sub_manifest', 'name', 'version')]),
        ),
    ]