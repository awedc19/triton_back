from django.conf.urls import path, url
from django.contrib import admin
from .views import BoardListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(routers.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('board/', BoardListAPI.as_view(), name='board'),
]