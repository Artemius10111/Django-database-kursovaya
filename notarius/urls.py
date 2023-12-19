# urls.py
from django.urls import path, include

from users.views import LogoutView
from .views import client_form_view, delete_service, notarius_service_list

urlpatterns = [
    path('notarius_add/', client_form_view, name='notarius_add_page'),
    path('delete_service/<uuid:pk>', delete_service, name="delete_service"),
    path('', notarius_service_list, name='notarius_service_list'),
    path('user/', include('users.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]