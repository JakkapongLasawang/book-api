from django.urls import path
from .views import BookList,FindOne

urlpatterns = [
    path('', BookList.as_view()),
    path('<int:book_id>', FindOne.as_view()),
]
