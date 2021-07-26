from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.views import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics

#Category
class CreateCategory(APIView):
    def post(self, request):
        serializer = CategorySerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#product creation
class CreateProduct(APIView):
    def post(self, request):
        serializer = ProductDetailsSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# product list
class ProductDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self , request):
       qs = Product.objects.all()
       prod = ProductDetailsSerilizer(qs, many= True)
       return Response(prod.data)

# product update
# class UpdatePassword(APIView):
#     def put(self, request,id):
#         product = Product.objects.get(id=id)
#         if product:
#             product.id = id
#             product.save()
#             return Response('data updated', status=status.HTTP_201_CREATED)
#         return Response('error occur', status=status.HTTP_304_NOT_MODIFIED)

# #product delete
# class ProductDelete(APIView):
#    def delete(self,id, format=None):
#         data = Product.objects.get(id=id)
#         data.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerilizer


class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerilizer