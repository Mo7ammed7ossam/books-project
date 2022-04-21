from django.urls import path
from .views import index, get_single_book, get_author, add_new_book, update_book_data, delete_book_data

urlpatterns = [
    path('', index, name='home_page'),

    path('books/<int:book_ISBN>', get_single_book, name='book_details'),

    path('books/add', add_new_book, name='create_book'),
    path('books/edit/<int:book_ISBN>', update_book_data, name='update_book'),
    path('books/delete/<int:book_ISBN>', delete_book_data, name='delete_book'),

    path('books/author/<int:author_id>', get_author, name='author_details'),

]
