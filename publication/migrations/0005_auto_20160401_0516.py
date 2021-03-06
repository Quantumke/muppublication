# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 10:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_subscribe_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='news_posts',
            name='active',
            field=models.CharField(default='active', max_length=100),
        ),
    ]
