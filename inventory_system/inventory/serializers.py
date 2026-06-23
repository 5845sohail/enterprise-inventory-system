from rest_framework import serializers
from inventory.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'quantity', 'date_added']     

def to_representation(self, instanse):                      #runs ONLY on outgoing GET read data streams
    representation = super().to_representation(instanse)
    representation['category'] = CategorySerializer(instanse.category).data
    return representation
