from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from sandrini_api.serializers import ChannelSerializer, CategorySerializer, ChannelDetailSerializer
from sandrini_test.models import Channel, Category


class ChannelViewSet(viewsets.ViewSet):
    def list(self, request):
        instance = Channel.objects.all()
        serializer = ChannelSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Channel, pk=pk)
        serializer = ChannelDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        instance = Category.objects.filter(top_category=None)
        serializer = CategorySerializer(instance, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk):
        instance = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance, context={'request': request})
        return Response(serializer.data)