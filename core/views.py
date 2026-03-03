from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required   # <-- ini yg lo bilang

def home(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # <-- ganti dari home ke dashboard
        else:
            messages.error(request, 'Username atau password salah')
    
    return render(request, 'core/login.html')

@login_required
def dashboard(request):

    context = {
        'hr_count': 156,
        'prod_count': 12450,
        'fin_total': 'Rp 2.4M',
        'hr_change': '+12',
        'prod_change': '+8%',
        'fin_change': '+15%',
    }
    return render(request, 'core/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')