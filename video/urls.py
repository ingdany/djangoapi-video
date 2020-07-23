from .views import ListVideo, DetailVideo
from django.urls import path, re_path

urlpatterns = [
    path('videos',ListVideo.as_view(), name='list-video'),
    re_path(r'^videos/(?P<pk>[0-9]+)$', DetailVideo.as_view(), name='detail-video')
]