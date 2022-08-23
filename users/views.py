from django.shortcuts import render,redirect
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
	if request.method == 'POST':
		r_form = RegisterForm(request.POST)
		if r_form.is_valid():
			r_form.save()
			username = r_form.cleaned_data.get('username')
			messages.success(request, f'Account registered for {username}')
			return redirect('login')

	else:
		r_form = RegisterForm()

	context = {
		'r_form':r_form
	}
	return render(request, 'users/register.html',context)

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)