from .views import ListVideo
from django.urls import path

urlpatterns = [
    path('videos',ListVideo.as_view(),name='list-video')
]