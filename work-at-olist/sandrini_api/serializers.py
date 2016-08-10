from rest_framework import serializers
from sandrini_test.models import Channel, Category


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField()
    channel = serializers.CharField()
    sub_categories = serializers.SerializerMethodField()
    top_category = serializers.CharField()

    def get_sub_categories(self, obj):
        categories = Category.objects.filter(top_category=obj)
        return CategorySerializer(categories, many=True).data

    class Meta:
        model = Category
        fields = ['name', 'slug', 'channel', 'sub_categories', 'top_category']
        lookup_field = 'slug'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    #top_category = serializers.CharField()
    name = serializers.CharField()
    sub_categories = serializers.SerializerMethodField()

    def get_sub_categories(self, obj):
        categories = Category.objects.filter(top_category=obj)
        return CategorySerializer(categories, many=True).data

    class Meta:
        model = Category
        fields = ['name', 'slug', 'sub_categories']
        lookup_field = 'slug'


class ChannelDetailSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField()
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        categories = Category.objects.filter(channel=obj, top_category=None)
        return CategorySerializer(categories, many=True).data

    class Meta:
        model = Channel
        fields = ['name', 'slug', 'categories']
        lookup_field = 'slug'


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['name', 'slug']
        lookup_field = 'slug'