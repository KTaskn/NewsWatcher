from rest_framework import viewsets
from .models import Newspaper, Word
from .serializers import NewspaperSerializer, WordSerializer

class NewspaperViewSet(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer
    http_method_names = ['get']

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    http_method_names = ['get']
