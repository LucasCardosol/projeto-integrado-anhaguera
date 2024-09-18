# api/urls.py
from django.urls import path
from .views import BookListCreate , BookList , BookDetail, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),

    # URL para listar todos os livros
    path('books/', BookList.as_view(), name='book-list'),
    
    # URL para obter um único livro pelo id
    path('books/<int:id>/', BookDetail.as_view(), name='book-detail'),

    # URL para atualizar um livro pelo id (PUT/PATCH)
    path('books/<int:id>/update/', BookUpdate.as_view(), name='book-update'),

    # URL para deletar um livro pelo id (DELETE)
    path('books/<int:id>/delete/', BookDelete.as_view(), name='book-delete'),
]
