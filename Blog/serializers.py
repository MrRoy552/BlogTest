from dataclasses import fields
from pyexpat import model

from Blogproject.settings import AUTH_USER_MODEL
from.models import*
from rest_framework import serializers,status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken




from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user



class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

    # def get_sku_count(self, obj):
    #     sku_count=Add_On_SKU.objects.filter(sku=[obj]).count()
    #     return sku_count