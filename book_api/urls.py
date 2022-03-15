from django.urls import path
from .views import BookList, BookCreate

urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
]
