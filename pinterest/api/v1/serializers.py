from rest_framework import serializers
from pinterest.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('type',)

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    cast = CastSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'