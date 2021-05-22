from django.contrib import admin
from django.db import router
from django.urls import path, include
from Contact import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact', views.ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('work/', include('Work.urls'))
]
