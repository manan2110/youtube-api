from .models import *
from .serializers import *

from rest_framework import generics


class YoutubeItems(generics.ListAPIView):
    ordering = "-publishedDateTime"
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
