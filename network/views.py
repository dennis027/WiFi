from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import ProfileUpdateForm, RegistrationForm, UserSubscriptionForm, UserUpdateForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import utc
from django.http import JsonResponse
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 


def logout_view(request):
    logout(request)
    return redirect('/')

def index (request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    subscribers=Subscriber.objects.all()
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request,'Your Profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context={'p_form': p_form, 'u_form': u_form,'subscribers':subscribers}
    return render(request, 'profile.html',context )

def review(request):
    subscribers=Subscriber.objects.all()

    return render(request, 'review.html',{"subscribers": subscribers})    

# def subscription(request):
    

#     return render(request, 'subscription.html')    

def userpage(request):
	user_form = UserUpdateForm(instance=request.user)
	profile_form = ProfileUpdateForm(instance=request.user.profile)
	return render(request=request, template_name="user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })




@login_required(login_url='/accounts/login/') 
def newsubscription(request):
    current_user = request.user
    if request.method == 'POST':
        form = UserSubscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.user = current_user
            subscriber.save()
        return redirect('profile')
    else:
        form = UserSubscriptionForm()
    return render(request, 'newsubscription.html',{'form':form}) 

@login_required(login_url='/accounts/login/') 
def change(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')
    user= sss
