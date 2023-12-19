from .models import User
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')