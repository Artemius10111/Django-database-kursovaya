# urls.py
from django.urls import path, include

from users.views import LogoutView
from .views import client_form_view, notarius_service_list

urlpatterns = [
    path('notarius_add/', client_form_view, name='notarius_add_page'),
    path('', notarius_service_list, name='notarius_service_list'),
    path('user/', include('users.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]