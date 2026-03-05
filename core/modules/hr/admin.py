from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nik', 'nama', 'jabatan', 'dept', 'status_karyawan', 'tgl_rekrut']
    list_filter = ['status_karyawan', 'dept', 'jabatan']
    search_fields = ['nama', 'nik', 'no_ktp']