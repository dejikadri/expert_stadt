# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email_address', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=200)),
                ('full_description', models.TextField()),
                ('university', models.CharField(max_length=250)),
                ('major', models.CharField(max_length=250)),
                ('popularity', models.IntegerField()),
                ('path_to_picture', models.CharField(max_length=150)),
                ('hourly_rate', models.FloatField()),
                ('total_hours_taught', models.IntegerField()),
            ],
        ),
    ]