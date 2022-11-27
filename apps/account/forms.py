from django import forms
from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class RegisterForm(UserCreationForm):
    '''A form that creates a user, with no privileges, from the given first_name, email and password.'''

    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'email')