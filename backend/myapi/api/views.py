# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View para listar e criar novos Books
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# View para listar todos os Books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# View para obter um único Book pelo id
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

# View para deletar um Book pelo id
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'