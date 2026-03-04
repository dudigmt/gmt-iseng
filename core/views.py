from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username atau password salah')
    
    return render(request, 'core/login.html')

@login_required
def dashboard(request):
    # CEK ROLE USER
    groups = request.user.groups.all()
    
    if request.user.is_superuser:
        role = 'Super Admin'
    elif groups.filter(name='HR').exists():
        role = 'HR Staff'
    elif groups.filter(name='Acc. & Fin.').exists():
        role = 'Finance Staff'
    elif groups.filter(name='Production').exists():
        role = 'Production Staff'
    elif groups.filter(name='Marketing').exists():
        role = 'Marketing Staff'
    elif request.user.is_staff:
        role = 'Admin'
    else:
        role = 'User'

    context = {
        'hr_count': 156,
        'prod_count': 12450,
        'fin_total': 'Rp 2.4M',
        'hr_change': '+12',
        'prod_change': '+8%',
        'fin_change': '+15%',
        'user_role': role,
    }
    return render(request, 'core/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')