from  rest_framework import serializers
from  .models import Author,Book
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Author
#         fields=('name',)


class BookSerializer(serializers.ModelSerializer):
    author=serializers.CharField(source='author_name.author_name')
    category=serializers.CharField(source='category_name.category_name')
    class Meta:
        model=Book
        fields=('pk','book_name','book_price','isbn_number','author','category')


class CreatebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name', 'book_price', 'isbn_number', 'author_name', 'category_name')


class DestroybookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('pk','book_name', 'book_price', 'isbn_number', 'author_name', 'category_name')


class UpdatebookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ('book_name', 'book_price', 'isbn_number', 'author_name', 'category_name')






