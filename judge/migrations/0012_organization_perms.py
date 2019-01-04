# -*- coding: utf-8 -*-


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0011_organization_is_open'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['key'], 'permissions': (('organization_admin', 'Administer organizations'),
                                                          ('edit_all_organization', 'Edit all organizations'))},
        ),
    ]
