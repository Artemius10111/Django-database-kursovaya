# urls.py
from django.urls import path
from .views import client_form_view

urlpatterns = [
    path('notarius_add/', client_form_view, name='notarius_add_page'),
    # Другие URL-маршруты вашего приложения
]