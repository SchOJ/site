# -*- coding: utf-8 -*-


import django.db.models.deletion
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0008_contestproblem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Associated problem', blank=True, to='judge.Problem', null=True),
            preserve_default=True,
        ),
    ]
