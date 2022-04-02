from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('practice/', include('practice.urls')),
    path('admin/', admin.site.urls),
]
