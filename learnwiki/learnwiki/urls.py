from django.urls import include
from django.contrib import admin
from django.urls import path

from lw_main.api import router


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]