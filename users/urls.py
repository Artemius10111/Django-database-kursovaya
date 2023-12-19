from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.SignUpView.as_view(), name="SignUp"),
    path('login/', views.LoginView.as_view(), name='login'),
]

