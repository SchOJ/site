# -*- coding: utf-8 -*-


import django.core.validators
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0009_solution_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='page',
            field=models.CharField(db_index=True, max_length=30, verbose_name=b'Associated Page', validators=[django.core.validators.RegexValidator(b'^[pc]:[a-z0-9]+$|^b:\\d+$|^s:', b'Page code must be ^[pc]:[a-z0-9]+$|^b:\\d+$')]),
            preserve_default=True,
        ),
    ]
