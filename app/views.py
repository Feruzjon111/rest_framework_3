from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        response = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
            'message': 'BookList',
        }
        return Response(response)


class BookCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
               'message': 'Book created successfully',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid data',
            }
        return Response(response)


class BookDelete(APIView):
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        response = {
            'data': None,
            'status': status.HTTP_204_NO_CONTENT,
           'message': 'Book deleted successfully',
        }
        return Response(response)



class BookUpdate(APIView):
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
               'message': 'Book updated successfully',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid data',
            }
        return Response(response)

    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
               'message': 'Book partially updated successfully',
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
               'message': 'Invalid data',
            }
        return Response(response)



class BookRetrieve(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        response = {
            'data': serializer.data,
            'status': status.HTTP_200_OK,
           'message': 'Book retrieved successfully',
        }
        return Response(response)


