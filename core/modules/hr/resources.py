from import_export import resources, fields
from import_export.widgets import DateWidget
from .models import Employee

class EmployeeResource(resources.ModelResource):
    tgl_lahir = fields.Field(attribute='tgl_lahir', widget=DateWidget(format='%d/%m/%Y'))
    tgl_rekrut = fields.Field(attribute='tgl_rekrut', widget=DateWidget(format='%d/%m/%Y'))
    tgl_kartetap = fields.Field(attribute='tgl_kartetap', widget=DateWidget(format='%d/%m/%Y'))
    kontrak_berakhir = fields.Field(attribute='kontrak_berakhir', widget=DateWidget(format='%d/%m/%Y'))
    tgl_out = fields.Field(attribute='tgl_out', widget=DateWidget(format='%d/%m/%Y'))
    
    class Meta:
        model = Employee
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('nik',)
        exclude = ('id', 'created_at', 'updated_at', 'import_batch', 'imported_at')
    
    def before_import_row(self, row, **kwargs):
        # Skip baris kosong (NIK kosong)
        if not row.get('nik') or str(row.get('nik')).strip() == '':
            return None  # Return None untuk skip baris ini
        
        # Set semua data import sebagai draft
        row['is_draft'] = True
        row['is_active'] = False
        return super().before_import_row(row, **kwargs)