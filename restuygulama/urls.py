from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from app1 import views
router = routers.DefaultRouter()
router.register(r'yazarlar', views.YazarViewSet)
router.register(r'kitaplar', views.KitapViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
]
