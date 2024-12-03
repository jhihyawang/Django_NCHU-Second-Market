from django import forms 
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	class Meta:
		model= User 
		fields=('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
		username=forms.CharField(label='姓名', max_length=10)
		password=forms.CharField(label='密碼', max_length=11 , widget=forms.PasswordInput())
		