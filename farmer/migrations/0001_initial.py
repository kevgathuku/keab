# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('variety', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('id_number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('farm_size', models.CharField(max_length=200)),
                ('crops', models.ManyToManyField(to='farmer.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration_passed', models.DurationField()),
                ('text', models.TextField()),
                ('crop', models.ForeignKey(to='farmer.Crop')),
                ('farmer', models.ForeignKey(to='farmer.Farmer')),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='crops',
            field=models.ManyToManyField(to='farmer.Crop'),
        ),
    ]
