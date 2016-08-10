from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from sandrini_api.serializers import ChannelSerializer, CategorySerializer, ChannelDetailSerializer, \
    CategoryDetailSerializer
from sandrini_test.models import Channel, Category


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Channel, slug=kwargs['slug'])
        serializer = ChannelDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(top_category=None)
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, slug=kwargs['slug'])
        serializer = CategoryDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)