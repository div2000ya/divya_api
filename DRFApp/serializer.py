from rest_framework import serializers
from .models import *

class CategorySerilizer(serializers.ModelSerializer):

    class Meta :
        model = Category
        fields = "__all__"

class ProductDetailsSerilizer(serializers.ModelSerializer):

    class Meta :
        model = Product
        fields = "__all__"
