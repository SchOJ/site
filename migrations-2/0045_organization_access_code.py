# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 16:05


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0044_organization_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='access_code',
            field=models.CharField(blank=True, help_text='Student access code', max_length=7, null=True, verbose_name='access code'),
        ),
    ]
