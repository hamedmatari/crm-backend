from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Buyer, Order

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['name','phone_number']

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = [
            'id',
            'created_at',
            'updated_at',
            'buyer_id',
            'count',
            'paper_type',
            'address',
            'price',
        ]



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    
    # fields haro az __all__ darbiar
    
    