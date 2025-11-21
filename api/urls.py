from django.urls import path
from . import views

urlpatterns = [
    # Exemple : on crée juste une route temporaire
    path('', views.home, name='api-home'),  # accessible via /api/
]
