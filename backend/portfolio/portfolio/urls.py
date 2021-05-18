from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('Contact.urls')),
    path('work/', include('Work.urls'))
]
