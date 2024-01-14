from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from app.models import Form
from django.contrib import messages

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def index(request):

    if request.user.is_anonymous:
        messages.warning(request, 'Not a valid user!!!')
        return redirect("/login")

    else:
        
        return render(request, 'index.html')

    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def Userlogin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)
            messages.success(request, 'Login succesfully...')
            return redirect('/')

        else:
            
            messages.warning(request, 'Not a valid user!!!')
            return render(request, "login.html")

    return render(request, "login.html")

    

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def Signup(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email = request.POST.get('email')

        if password != password2:
            messages.warning(request, 'Pasword does not match!!!')
            return redirect('signup')

        else:

            user = User.objects.create_user(username=username, password=password)
            user.save()

            con = Form(username=username, password=password, password2=password2, name=name, tel=tel, email=email)
            con.save()

            messages.success(request, 'User crate succesfully....')
            return render(request, 'login.html')


    return render(request, 'signup.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def Userlogout(request):

        logout(request)
        messages.success(request, 'Succesfully logout...')
        return render(request, 'login.html')
      