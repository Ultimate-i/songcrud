# Generated by Django 4.1.2 on 2022-10-27 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0009_rename_music_id_lyric_the_song_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='the_song_id',
            new_name='the_id',
        ),
    ]
