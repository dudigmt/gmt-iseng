import pandas as pd
from django.core.management.base import BaseCommand
from core.modules.hr.models import Employee
from datetime import datetime
import uuid

class Command(BaseCommand):
    help = 'Test import 1 baris'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        df = pd.read_excel(options['file_path'])
        batch = uuid.uuid4()
        
        for index, row in df.iterrows():
            try:
                print(f"\n--- Baris {index+1} ---")
                
                # Mapping manual
                data = {
                    'nik': str(row.get('nik', '')),
                    'nama': row.get('nama', ''),
                    'sex': row.get('sex', 'L')[:1],
                    'tgl_lahir': self.parse_date(row.get('tgl_lahir')),
                    'tempat_lahir': row.get('tempat_lahir', ''),
                    'no_hp': str(row.get('no_hp', '')),
                    'alamat': row.get('alamat', ''),
                    'kelurahan': row.get('kelurahan', ''),
                    'kecamatan': row.get('kecamatan', ''),
                    'kabupaten_kota': row.get('kabupaten_kota', ''),
                    'provinsi': row.get('provinsi', ''),
                    'no_ktp': str(row.get('no_ktp', '')),
                    'tgl_rekrut': self.parse_date(row.get('tgl_rekrut')),
                    'status_karyawan': row.get('status_karyawan', 'Kontrak'),
                    'jabatan': row.get('jabatan', ''),
                    'dept': row.get('dept', ''),
                    'is_draft': True,
                    'is_active': False,
                    'import_batch': batch,
                }
                
                # Print data yang akan diinsert
                for key, value in data.items():
                    print(f"{key}: {value} ({type(value)})")
                
                # Coba insert
                emp = Employee.objects.create(**data)
                print(f"✅ Berhasil: {emp.nama}")
                
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                import traceback
                traceback.print_exc()
    
    def parse_date(self, value):
        if pd.isna(value):
            return None
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d').date()
            except:
                return datetime.strptime(value, '%d/%m/%Y').date()
        return None