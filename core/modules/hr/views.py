from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .form import EmployeeForm

@login_required
def hr_dashboard(request):
    context = {
        'total_karyawan': Employee.objects.count(),
        # tambah data dummy lain sesuai kebutuhan
    }
    return render(request, 'hr/dashboard.html', context)

@login_required
def employee_list(request):
    employees = Employee.objects.all().order_by('-tgl_masuk')
    return render(request, 'hr/employee_list.html', {'employees': employees})

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