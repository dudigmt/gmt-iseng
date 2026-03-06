from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee
from .resources import EmployeeResource

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ['nik', 'nama', 'jabatan', 'dept', 'status_karyawan', 'is_draft', 'is_active', 'import_batch']
    list_filter = ['status_karyawan', 'dept', 'jabatan', 'is_draft', 'is_active', 'import_batch']
    search_fields = ['nama', 'nik', 'no_ktp']
    actions = ['approve_selected', 'activate_selected']
    
    def approve_selected(self, request, queryset):
        # Ubah draft jadi non-draft
        queryset.update(is_draft=False)
        self.message_user(request, f"{queryset.count()} data telah di-approve")
    approve_selected.short_description = "Approve selected data"
    
    def activate_selected(self, request, queryset):
        # Nonaktifkan semua data aktif dulu, lalu aktifkan yang dipilih
        Employee.objects.filter(is_active=True).update(is_active=False)
        queryset.update(is_active=True, is_draft=False)
        self.message_user(request, f"{queryset.count()} data telah diaktifkan")
    activate_selected.short_description = "Activate selected data"