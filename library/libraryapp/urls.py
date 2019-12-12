from django.urls import path,include
from .views import BookListAPIView,BookCreateAPIView,BookDestroyAPTView,BookUpdateAPIView

urlpatterns = [
   path('book/',BookListAPIView.as_view(), name='book-list'),
   path('book/create',BookCreateAPIView.as_view(),name='book-create'),
   path('book/destroy/<int:pk>/',BookDestroyAPTView.as_view(),name='book-destroy'),
   path('book/update/<int:pk>',BookUpdateAPIView.as_view(),name='book-update')

   ]

