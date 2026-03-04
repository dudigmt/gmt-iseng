from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nik', 'nama', 'departemen', 'posisi', 'tgl_masuk', 'gaji']
    list_filter = ['departemen', 'posisi']
    search_fields = ['nama', 'nik']