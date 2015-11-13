# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20151113_1404'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='crops',
        ),
        migrations.AddField(
            model_name='order',
            name='crops',
            field=models.ForeignKey(default=1, to='farmer.Crop'),
            preserve_default=False,
        ),
    ]
