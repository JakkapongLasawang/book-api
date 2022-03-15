from rest_framework.views import APIView
from rest_framework.response import Response


class BookList(APIView):
    def get(self, request):
        return Response({
            "status": "GET"
        })

class BookCreate(APIView):
    def post(self, request):
        return Response({
            "status": "POST"
        })
