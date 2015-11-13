# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='crops',
        ),
        migrations.AddField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(to='farmer.Buyer'),
        ),
        migrations.AddField(
            model_name='order',
            name='crops',
            field=models.ManyToManyField(to='farmer.Crop'),
        ),
    ]
