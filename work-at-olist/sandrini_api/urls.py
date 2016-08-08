from django.conf.urls import url, include
from rest_framework import routers
from sandrini_api.views import ChannelViewSet, schema_view, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet, base_name='channels')
router.register(r'categories', CategoryViewSet, base_name='categories')

urlpatterns = [
    url('doc/', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]