
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ['id','title', 'number_of_pages', 'author', 'quantity']
        fields = '__all__'
