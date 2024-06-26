from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price', 'stock', 'description', 'category', 'category_name']
        extra_kwargs = {
            'category': {'write_only': True}
        }

    def get_category_name(self, obj):
        return obj.category.category_name

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class OrderSerializer(serializers.ModelSerializer):
    user_fullname = serializers.SerializerMethodField()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    product_name = serializers.SerializerMethodField()
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_fullname', 'product_name', 'quantity', 'contact_no', 'address', 'PAYMENT', 'user', 'product']
        extra_kwargs = {
            'user': {'write_only': True},
            'product': {'write_only': True}
        }

    def get_user_fullname(self, obj):
        # return obj.user.first_name+last_name
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_product_name(self, obj):
        return obj.product.product_name