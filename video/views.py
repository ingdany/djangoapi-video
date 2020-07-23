from django.shortcuts import render
from .models import Video
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VideoSerializer

# Create your views here.
class ListVideo(APIView):
    def get(self, request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True)
        return Response(video_json.data)
    
    def post(self, request):
        video_json = VideoSerializer(data = request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data, status= 201)
        return Response(video_json.errors, status= 400)