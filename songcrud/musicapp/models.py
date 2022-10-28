from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + "" + self.last_name

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()

    def __str__(self):
         return self.title

class Lyric(models.Model):
    song = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=100000)

    def __str__(self):
        return self.content