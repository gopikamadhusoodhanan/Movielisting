from django.shortcuts import render, redirect,get_object_or_404
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):

    return render(request, 'index.html')
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
        else:
            print("invalid registration")
    context = {'registerform':form}
    return render(request, 'register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("movie:dashboard")
    context = {'loginform':form}
    return render(request, 'my-login.html', context=context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

