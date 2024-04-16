from django.contrib import admin
from django.urls import path
from book.views import hello_view, main_view, fun_view, list_books_view, book_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", main_view),
    path("hello/", hello_view),
    path("fun/", fun_view),
    path("books/", list_books_view),
    path("books/<int:book_id>/", book_detail_view),
]



