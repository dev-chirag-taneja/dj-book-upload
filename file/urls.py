from django.urls import path

from .views import *

urlpatterns = [
    # path("upload/", upload, name="upload"),
    path("books/", list_book, name="list_book"),
    path("books/upload/", upload_book, name="upload_book"),
    path("books/delete/<str:pk>/", delete_book, name="delete_book"),
]
