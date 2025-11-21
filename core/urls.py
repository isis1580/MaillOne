from django.contrib import admin
from django.urls import path, include
from website import views as website_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website_views.home, name='home'),
    path('api/', include('api.urls')),  # si tu as un fichier api/urls.py
]
