from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date'}),
            'tgl_rekrut': forms.DateInput(attrs={'type': 'date'}),
            'tgl_kartetap': forms.DateInput(attrs={'type': 'date'}),
            'kontrak_berakhir': forms.DateInput(attrs={'type': 'date'}),
            'tgl_out': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white'
            })