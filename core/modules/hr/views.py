from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Employee
from .forms import EmployeeForm

@login_required
def hr_dashboard(request):
    context = {
        'total_karyawan': Employee.objects.count(),
        'karyawan_aktif': Employee.objects.filter(status_kerja=True).count(),
        'karyawan_kontrak': Employee.objects.filter(status_karyawan='Kontrak').count(),
        'karyawan_tetap': Employee.objects.filter(status_karyawan='Tetap').count(),
    }
    return render(request, 'hr/dashboard.html', context)

@login_required
def employee_list(request):
    employees_list = Employee.objects.all().order_by('-tgl_rekrut')
    
    total_karyawan = employees_list.count()
    aktif = employees_list.filter(status_kerja=True).count()
    kontrak = employees_list.filter(status_karyawan='Kontrak').count()
    tetap = employees_list.filter(status_karyawan='Tetap').count()
    
    departemen_list = Employee.objects.values_list('dept', flat=True).distinct().order_by('dept')
    
    paginator = Paginator(employees_list, 20)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    
    context = {
        'employees': employees,
        'total_karyawan': total_karyawan,
        'aktif': aktif,
        'kontrak': kontrak,
        'tetap': tetap,
        'departemen_list': departemen_list,
    }
    return render(request, 'hr/employee_list.html', context)

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr:employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'hr/employee_form.html', {'form': form, 'title': 'Tambah Karyawan'})