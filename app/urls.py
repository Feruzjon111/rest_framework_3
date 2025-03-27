# from .views import BookViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'book', BookViewSet, basename='book')
# urlpatterns = router.urls

from django.urls import path
from .views import BookList, BookCreate, BookDelete, BookUpdate, BookRetrieve


urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', BookCreate.as_view(), name='book_create'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='book_update'),
    path('retrieve/<int:pk>/', BookRetrieve.as_view(), name='book_retrieve'),
]