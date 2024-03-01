from django.shortcuts import render
from rest_framework import generics


from books.models import Books
from .serializers import BookSerializer
# Create your views here.


class BookApiListView(generics.ListAPIView):

    queryset = Books.objects.all()
    serializer_class = BookSerializer
