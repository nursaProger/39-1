import datetime
import random
from datetime import datetime

from django.shortcuts import render, HttpResponse
from book.models import Book

def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello! It's my project")


def main_view(request):
    date = datetime.now().date()
    time = datetime.now().time()
    if request.method == "GET":
        return render(request, 'main.html', context={'date': date, 'time':time})


def fun_view(request):
    if request.method == "GET":
        fs = ['Охота это спорт, особенно когда патроны закончились, а кабан еще жив.. ',
              'Для настоящего мужчины помочь по хозяйству означает поднять ноги, когда жена подметает',
              'Когда сынок графа дракулы не пришел домой с уроков, его мама решила, что ему кол поставили']

        rand = random.choice(fs)
        return HttpResponse(rand)

def list_books_view(request):
    if request.method == "GET":
        books = Book.objects.all()
        context = {'books':books}

        return render(request, "book/list_books.html", context)


def book_detail_view(request, book_id):
    if request == "GET":

        book = Book.objects.get(id=book_id)
        context = {'book': book}

        return render(request, 'book/book_detail.html', context)








