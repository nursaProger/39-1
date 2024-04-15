from django.contrib import admin
from django.urls import path
from book.views import hello_view, main_view, fun_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", main_view),
    path("hello/", hello_view),
    path("fun/", fun_view)
]



