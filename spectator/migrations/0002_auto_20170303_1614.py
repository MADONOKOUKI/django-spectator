# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='concert_title',
            field=models.CharField(blank=True, help_text="Optional. e.g., 'Indietracks 2017', 'Radio 1 Roadshow'.", max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, help_text='Automatically created so each Event has an appropriate title.', max_length=255),
        ),
    ]