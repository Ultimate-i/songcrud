from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

# Create your views here.
def index(request):
    return HttpResponse("All about my musicapp.")

def artiste_list(request):
    artistes = Artiste.objects.all()
    serializer = ArtisteSerializer(artistes, many=True)
    return JsonResponse({'Artistes': serializer.data}, safe=False)

def song_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return JsonResponse({'Songs': serializer.data}, safe=False)

def lyric_list(request):
    lyrics = Lyric.objects.all()
    serializer = LyricSerializer(lyrics, many=True)
    return JsonResponse({'Lyrics': serializer.data}, safe=False)