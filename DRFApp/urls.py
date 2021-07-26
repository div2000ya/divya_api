from django.contrib import admin
from django.urls import path, include
from DRFApp.views import *


urlpatterns = [
    path('category/',CreateCategory.as_view()),
    path('create/',CreateProduct.as_view()),
    path('details/',ProductDetail.as_view()),
    path('update/<int:pk>',ProductUpdate.as_view()),
    path('delete/<int:pk>/',ProductDelete.as_view()),
]