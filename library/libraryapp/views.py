from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,UpdateAPIView
from .models import Book
from .serilizer import BookSerializer,CreatebookSerializer,DestroybookSerializer,UpdatebookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreatebookSerializer


class BookDestroyAPTView(DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=DestroybookSerializer
    lookup_field = "pk"

class BookUpdateAPIView(UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=UpdatebookSerializer
    lookup_field = "pk"




# Create your views here.
