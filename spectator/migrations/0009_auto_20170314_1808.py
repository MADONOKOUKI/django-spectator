# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:08
from __future__ import unicode_literals

from django.db import migrations
import spectator.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spectator', '0008_auto_20170309_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'ordering': ('name_sort',)},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('title_sort',)},
        ),
        migrations.AlterModelOptions(
            name='publicationseries',
            options={'ordering': ('title_sort',), 'verbose_name_plural': 'Publication series'},
        ),
        migrations.RemoveField(
            model_name='creator',
            name='sort_name',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='sort_title',
        ),
        migrations.RemoveField(
            model_name='publicationseries',
            name='sort_title',
        ),
        migrations.AddField(
            model_name='creator',
            name='name_individual_sort',
            field=spectator.fields.PersonNaturalSortField('name', db_index=True, default='', editable=False, help_text="For sorting individuals. e.g. 'adams, douglas'.", max_length=255),
        ),
        migrations.AddField(
            model_name='creator',
            name='name_individual_sort_display',
            field=spectator.fields.PersonDisplayNaturalSortField('name', db_index=True, default='', editable=False, help_text="For displaying sorted individuals. e.g. 'Adams, Douglas'.", max_length=255),
        ),
        migrations.AddField(
            model_name='creator',
            name='name_sort',
            field=spectator.fields.NaturalSortField('name', db_index=True, default='', editable=False, help_text="Best for sorting groups. e.g. 'long blondes, the'.", max_length=255),
        ),
        migrations.AddField(
            model_name='publication',
            name='title_sort',
            field=spectator.fields.NaturalSortField('title', db_index=True, default='', editable=False, help_text="e.g. 'clockwork orange, a' or 'world cities, the'.", max_length=255),
        ),
        migrations.AddField(
            model_name='publicationseries',
            name='title_sort',
            field=spectator.fields.NaturalSortField('title', db_index=True, default='', editable=False, help_text="e.g. 'london review of books, the'.", max_length=255),
        ),
    ]