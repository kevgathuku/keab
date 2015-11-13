# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20151113_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 11, 13, 16, 36, 58, 127453, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
