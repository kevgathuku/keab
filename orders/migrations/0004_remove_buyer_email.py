# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_buyer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='email',
        ),
    ]
