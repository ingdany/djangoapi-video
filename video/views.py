from django.shortcuts import render
from .models import Video
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ListVideo(APIView):
    def get(self, request):
        videos = Video.objects.all()
        return Response(videos)