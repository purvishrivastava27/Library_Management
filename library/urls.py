from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),


    path(
        'books/',
        views.BookListView.as_view(),
        name='book_list'
    ),


    path(
        'books/add/',
        views.BookCreateView.as_view(),
        name='book_create'
    ),


    path(
        'books/<int:pk>/edit/',
        views.BookUpdateView.as_view(),
        name='book_update'
    ),


    path(
        'books/<int:pk>/delete/',
        views.BookDeleteView.as_view(),
        name='book_delete'
    ),


    path(
        'books/<int:pk>/borrow/',
        views.borrow_book,
        name='borrow_book'
    ),


    path(
        'books/<int:pk>/return/',
        views.return_book,
        name='return_book'
    ),


    path(
        'search/',
        views.search_books,
        name='search_books'
    ),

]