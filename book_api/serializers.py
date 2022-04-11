
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    # change field name
    # new_title = serializers.CharField(source='title')

    """ https://www.django-rest-framework.org/api-guide/fields/"""
    # django rest framework method serializer
    # it read only --not get input
    new_number_of_pages = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()

    class Meta:
        model = Book

        """Just select all fields or __all__ or exclude"""

        # fields = ['id','title', 'number_of_pages', 'author', 'quantity']
        fields = '__all__'
        # exclude = ['number_of_pages']

    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)
        # custom error messages
        self.fields['title'].error_messages['required'] = 'My custom required msg'

    def get_food(self, obj):
        # print(obj.__dict__)
        return "Food id is read only"

    def get_new_number_of_pages(self, obj):
        return obj.number_of_pages*25


class ReadBookSerializer(serializers.ModelSerializer):

    newTitle = serializers.SerializerMethodField()
    newNumberOfPages = serializers.SerializerMethodField()
    newAuthor = serializers.SerializerMethodField()
    newQuantity = serializers.SerializerMethodField()
    newPublished = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # fields = ['id','title', 'number_of_pages', 'author', 'quantity']
        fields = '__all__'

    def get_newTitle(self, obj):
        return obj.title

    def get_newNumberOfPages(self, obj):
        return obj.number_of_pages

    def get_newAuthor(self, obj):
        return obj.author

    def get_newQuantity(self, obj):
        return obj.quantity

    def get_newPublished(self, obj):
        return obj.published

    # Override so we can remove unwatned fields
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep["title"]
        del rep["number_of_pages"]
        del rep["author"]
        del rep["quantity"]
        del rep["published"]
        return rep
