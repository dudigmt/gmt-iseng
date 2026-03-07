from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    # Grouping fields untuk template
    personal_fields = ['nik', 'nama', 'sex', 'tgl_lahir', 'tempat_lahir']
    contact_fields = ['no_hp', 'alamat', 'kelurahan', 'kecamatan', 'kabupaten_kota', 'provinsi', 'kode_pos', 'no_ktp', 'no_kk']
    status_fields = ['status_kawin', 'tanggungan', 'agama']
    fisik_fields = ['tinggi_badan', 'berat_badan', 'gol_darah']
    pendidikan_fields = ['pendidikan']
    pekerjaan_fields = ['tgl_rekrut', 'status_karyawan', 'tgl_kartetap', 'jabatan', 'dept', 'posisi_karyawan']
    kontrak_fields = ['kontrak_ke', 'kontrak_berakhir']
    bank_fields = ['no_rek_bank', 'kode_bank', 'nama_bank']
    bpjs_fields = ['bpjs_tk', 'bpjs_tk_no', 'bpjs_kes', 'bpjs_kes_no']
    pajak_fields = ['status_ptkp', 'no_npwp', 'status_pajak']
    lain_fields = ['faskes', 'placement', 'foto']
    keluar_fields = ['tgl_out', 'status_kerja']
    
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'tgl_rekrut': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'tgl_kartetap': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'kontrak_berakhir': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'tgl_out': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'sex': forms.Select(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'status_kawin': forms.Select(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'status_karyawan': forms.Select(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent'}),
            'gol_darah': forms.TextInput(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Contoh: O, A, B, AB'}),
            'tinggi_badan': forms.NumberInput(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'dalam cm'}),
            'berat_badan': forms.NumberInput(attrs={'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'dalam kg'}),
            'bpjs_tk': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'}),
            'bpjs_kes': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'}),
            'status_kerja': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set required fields
        required_fields = ['nik', 'nama', 'tgl_lahir', 'tgl_rekrut', 'status_karyawan', 'jabatan', 'dept']
        for field in required_fields:
            self.fields[field].required = True
        
        # Set labels
        self.fields['sex'].label = 'Jenis Kelamin'
        self.fields['no_hp'].label = 'No. HP'
        self.fields['no_ktp'].label = 'No. KTP'
        self.fields['no_kk'].label = 'No. KK'
        self.fields['tgl_rekrut'].label = 'Tanggal Rekrut'
        self.fields['tgl_kartetap'].label = 'Tanggal Karyawan Tetap'
        self.fields['dept'].label = 'Departemen'
        self.fields['bpjs_tk_no'].label = 'No. BPJS TK'
        self.fields['bpjs_kes_no'].label = 'No. BPJS Kesehatan'
        self.fields['no_npwp'].label = 'No. NPWP'
        self.fields['tgl_out'].label = 'Tanggal Keluar'
        self.fields['status_kerja'].label = 'Status Aktif'
        
        # Add placeholder untuk text fields
        placeholder_fields = ['nik', 'nama', 'tempat_lahir', 'no_hp', 'no_ktp', 'no_kk', 
                              'kelurahan', 'kecamatan', 'kabupaten_kota', 'provinsi', 'kode_pos',
                              'jabatan', 'dept', 'posisi_karyawan', 'no_rek_bank', 'kode_bank',
                              'nama_bank', 'bpjs_tk_no', 'bpjs_kes_no', 'no_npwp', 'faskes', 'placement']
        
        for field in placeholder_fields:
            if field in self.fields:
                current_attrs = self.fields[field].widget.attrs
                self.fields[field].widget.attrs.update({
                    'placeholder': f'Masukkan {self.fields[field].label.lower()}'
                })
        
        # Styling untuk semua field text
        for field in self.fields:
            if field not in ['bpjs_tk', 'bpjs_kes', 'status_kerja']:  # Skip checkbox
                if 'class' not in self.fields[field].widget.attrs:
                    self.fields[field].widget.attrs.update({
                        'class': 'w-full px-4 py-2.5 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow text-gray-700 dark:text-gray-200'
                    })