from django.conf.urls import url, include
from rest_framework import routers
from sandrini_api.views import ChannelViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet, base_name='channels')
router.register(r'categories', CategoryViewSet, base_name='categories')

urlpatterns = [
    url('^docs/', include('rest_framework_swagger.urls'), name='docs-index'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]