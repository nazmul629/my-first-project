from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import *






def user_login(request):
    if request.method =="POST":
        form = UserLoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]

            user =authenticate(username=username, password=password)
           
            print(user)

            if user:
                login(request,user)
                return redirect("creat_result_urls")

            else:
                errMsg = "Username or password invalid"
                context = {'errMsg':errMsg,
                           'forms':form }
                return render(request,'myaut/user_login.html', context)

    form = UserLoginForms()
    context = {'forms':form}
    return render(request,'myaut/user_login.html', context)



def  user_logout(request):
    logout(request)
    return redirect("user_login_url")


def user_signup(request):
    if request.method == 'POST':
        forms = UserSiginUpForms(request.POST)
        if forms.is_valid():

            #collect forms data
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]
            re_password = forms.cleaned_data["re_password"]
            email = forms.cleaned_data["email"]

            #chak both password is same
            if password != re_password:
                errMsg = "Password and Re Password not same"
                context = {'errMsg':errMsg,
                            'form':forms}
                return render(request,'myaut/signup.html',context)

            # Cereate new User 
            User.objects.create_user(username,email,password)
            return redirect("user_login_url")
        
    forms = UserSiginUpForms()
    context ={'form':forms}
    return render(request,'myaut/signup.html',context)