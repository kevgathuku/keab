# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_auto_20151113_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='crops',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
