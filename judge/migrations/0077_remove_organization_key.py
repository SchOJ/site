# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 16:22


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0076_problem_statistics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name'], 'permissions': (('organization_admin', 'Administer organizations'), ('edit_all_organization', 'Edit all organizations')), 'verbose_name': 'organization', 'verbose_name_plural': 'organizations'},
        ),
        migrations.RemoveField(
            model_name='organization',
            name='key',
        ),
    ]
