from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book_submit', views.book_submit),
    path('author', views.author),
    path('author_submit', views.author_submit),
    path('books/<int:book_id>', views.book_display),
    path('authors/<int:author_id>', views.author_display),
    path('book_add', views.book_add),
    path('author_add', views.author_add)
]