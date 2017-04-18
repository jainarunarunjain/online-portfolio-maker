from django.shortcuts import render,redirect, get_object_or_404
from .forms import loginform,signupform, UserProfileForm
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from .models import UserProfile

# Create your views here.

def login_view(request):
	login_of_user = forms.loginform(request.POST or None)
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		users = authenticate(username=username, password=password)
		if users is not None:
			if users.is_active:
				auth_login(request, users)
				return redirect('/profile/')
		else:
			return HttpResponse("username and password didn't match ")

	context = {
		'login_of_user': login_of_user,
	}
	return render(request, 'login.html', context)

def signup_view(request):
	signup_of_user = forms.signupform(request.POST or None)
	if signup_of_user.is_valid():
		user = signup_of_user.save(commit=False)
		username = signup_of_user.cleaned_data['username']
		password = signup_of_user.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return redirect('/profile/')

	context = {
		'signup_of_user': signup_of_user,
	}
	return render(request, 'signup.html', context)

@login_required
def myprofile_view(request):
	form = UserProfileForm(request.POST or None, request.FILES or None, instance = request.user.profile)
	if form.is_valid():
		profile = form.save(commit=False)
		profile.user = request.user
		profile.save()
		return HttpResponse("Successfully created your Portfolio <br> click this link to see your portfolio : <a href='/theme1'>myportfolio</a>")

	context = {
		'form': form,
	}
	return render(request, 'profile.html', context)

def logout_view(request):
	logout(request)
	return HttpResponse("<h1>You Are Logged Out Successfully</h1>")

def themeoneview(request):
	instance = UserProfile.objects.get(user=request.user)
	context = {
		'instance' : instance,
	}
	return render(request, 'port1.html', context)
