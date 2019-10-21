from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_no=forms.IntegerField(required=False)
    email = forms.EmailField( help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'phone_no', 'email', 'password1', 'password2')