# Generated by Django 4.1.2 on 2022-10-27 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0012_rename_artiste_id_song_artist_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='music_id',
            new_name='Song_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Artiste',
            new_name='Artiste_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artist_id',
            new_name='artiste_id',
        ),
        migrations.RemoveField(
            model_name='lyric',
            name='Song',
        ),
    ]
