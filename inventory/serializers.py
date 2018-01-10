from rest_framework import serializers

from .models import Category, Profile, PackingList, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'weight', 'price', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'items')


class PackingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingList
        fields = ('id', 'name', 'user')
