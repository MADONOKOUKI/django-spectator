# Generated by Django 2.0 on 2018-02-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectator_events', '0032_recreate_work_slugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classicalwork',
            name='creators',
        ),
        migrations.RemoveField(
            model_name='classicalworkrole',
            name='classical_work',
        ),
        migrations.RemoveField(
            model_name='classicalworkrole',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='classicalworkselection',
            name='event',
        ),
        migrations.RemoveField(
            model_name='classicalworkselection',
            name='work',
        ),
        migrations.RemoveField(
            model_name='dancepiece',
            name='creators',
        ),
        migrations.RemoveField(
            model_name='dancepiecerole',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='dancepiecerole',
            name='dance_piece',
        ),
        migrations.RemoveField(
            model_name='dancepieceselection',
            name='event',
        ),
        migrations.RemoveField(
            model_name='dancepieceselection',
            name='work',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='creators',
        ),
        migrations.RemoveField(
            model_name='movierole',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='movierole',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movieselection',
            name='event',
        ),
        migrations.RemoveField(
            model_name='movieselection',
            name='work',
        ),
        migrations.RemoveField(
            model_name='play',
            name='creators',
        ),
        migrations.RemoveField(
            model_name='playrole',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='playrole',
            name='play',
        ),
        migrations.RemoveField(
            model_name='playselection',
            name='event',
        ),
        migrations.RemoveField(
            model_name='playselection',
            name='work',
        ),
        migrations.AlterField(
            model_name='event',
            name='kind',
            field=models.CharField(choices=[('concert', 'Classical'), ('comedy', 'Comedy'), ('dance', 'Dance'), ('exhibition', 'Exhibition'), ('gig', 'Gig'), ('misc', 'Other'), ('movie', 'Movie'), ('play', 'Theatre')], max_length=20),
        ),
        migrations.DeleteModel(
            name='ClassicalWork',
        ),
        migrations.DeleteModel(
            name='ClassicalWorkRole',
        ),
        migrations.DeleteModel(
            name='ClassicalWorkSelection',
        ),
        migrations.DeleteModel(
            name='DancePiece',
        ),
        migrations.DeleteModel(
            name='DancePieceRole',
        ),
        migrations.DeleteModel(
            name='DancePieceSelection',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='MovieRole',
        ),
        migrations.DeleteModel(
            name='MovieSelection',
        ),
        migrations.DeleteModel(
            name='Play',
        ),
        migrations.DeleteModel(
            name='PlayRole',
        ),
        migrations.DeleteModel(
            name='PlaySelection',
        ),
    ]
