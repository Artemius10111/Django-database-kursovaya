from django.shortcuts import render
from django.contrib.auth import views as django_views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
class LoginView(django_views.LoginView):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile', request.user.id)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    model = User
    success_url = reverse_lazy("SignUp")
    template_name = 'account/registration.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile', request.user.id)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return redirect('login')