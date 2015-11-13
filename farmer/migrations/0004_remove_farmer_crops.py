# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20151113_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='crops',
        ),
    ]
