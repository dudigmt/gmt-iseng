from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employee

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