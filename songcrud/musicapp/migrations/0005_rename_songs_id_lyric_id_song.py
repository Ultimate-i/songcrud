# Generated by Django 4.1.2 on 2022-10-27 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_rename_song_id_lyric_songs_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='songs_id',
            new_name='id_song',
        ),
    ]
