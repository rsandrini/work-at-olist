from rest_framework import serializers
from sandrini_test.models import Channel, Category


class CategorySerializer(serializers.ModelSerializer):
    top_category = serializers.CharField()
    name = serializers.CharField()
    sub_categories = serializers.SerializerMethodField()

    def get_sub_categories(self, obj):
        categories = Category.objects.filter(top_category=obj)
        return CategorySerializer(categories, many=True).data

    class Meta:
        model = Category
        exclude = ['id', 'channel', 'top_category']


class ChannelDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        categories = Category.objects.filter(channel=obj, top_category=None)
        return CategorySerializer(categories, many=True).data

    class Meta:
        model = Channel
        fields = ['name', 'categories']


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['name',]