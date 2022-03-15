from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class FindOne(APIView):
    def get_book_by_id(self, book_id):
        return Book.objects.get(id=book_id)

    def get(self, request, book_id):
        book = None
        try:
            book = self.get_book_by_id(book_id)
        except:
            return Response({'error': 'Book not found'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = self.get_book_by_id(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, book_id):
        book = self.get_book_by_id(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
