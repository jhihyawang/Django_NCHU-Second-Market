from django.shortcuts import render
from item.models import Category,Item
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import forms
from item.models import Category,Item
from django.contrib.auth import authenticate
from django.contrib import auth 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def contact(request):
    return render(request,'accounts/contact.html')

def signup(request):
	if request.method=='POST':
		form=forms.SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login/')
	else:
		form=forms.SignupForm()
	return render(request,'accounts/signup.html', locals())


def login(request):
	if request.method=='POST':
		login_form=forms.LoginForm(request.POST)
		if login_form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user= authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					auth.login(request,user)
					messages.add_message(request, messages.SUCCESS, '登入成功')
					return HttpResponseRedirect('/')
				else:
					messages.add_message(request, messages.WARNING, '帳號尚未啟用')
					
			else:
				messages.add_message(request, messages.WARNING, '登入失敗')
				
		else:
			messages.add_message(request, messages.WARNING, '請檢查輸入欄位')
			
	else:
		login_form=forms.LoginForm()


	return render(request, 'accounts/login.html', locals())

def logout(request):
	auth.logout(request)
	messages.add_message(request,messages.INFO,'登出成功')
	return HttpResponseRedirect('/')
