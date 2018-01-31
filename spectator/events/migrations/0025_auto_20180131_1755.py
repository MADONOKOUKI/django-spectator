# Generated by Django 2.0 on 2018-01-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_events', '0024_event_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='cinema_treasures_id',
            field=models.PositiveIntegerField(blank=True, help_text='Optional. ID of a cinema at <a href="http://cinematreasures.org/">Cinema Treasures</a>.', null=True),
        ),
    ]
