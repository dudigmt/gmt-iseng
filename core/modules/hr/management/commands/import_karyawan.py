import pandas as pd
from django.core.management.base import BaseCommand
from core.modules.hr.models import Employee
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data karyawan dari file Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path ke file Excel')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        # Baca Excel
        df = pd.read_excel(file_path)
        
        success = 0
        failed = 0
        
        for index, row in df.iterrows():
            try:
                # Mapping kolom Excel ke field model
                Employee.objects.update_or_create(
                    nik=str(row['nik']),
                    defaults={
                        'nama': row['nama'],
                        'sex': row['sex'],
                        'tgl_lahir': self.parse_date(row['tgl_lahir']),
                        'tempat_lahir': row['tempat_lahir'],
                        'no_ktp': str(row['no_ktp']),
                        'no_kk': str(row['no_kk']),
                        'no_hp': str(row['no_hp']),
                        'alamat': row['alamat'],
                        'kelurahan': row['kelurahan'],
                        'kecamatan': row['kecamatan'],
                        'kabupaten_kota': row['kabupaten_kota'],
                        'kode_pos': str(row['kode_pos']),
                        'provinsi': row['provinsi'],
                        'status_kawin': row['status_kawin'],
                        'tanggungan': int(row['tanggungan']) if pd.notna(row['tanggungan']) else 0,
                        'agama': row['agama'],
                        'tinggi_badan': int(row['tinggi_badan']) if pd.notna(row['tinggi_badan']) else 0,
                        'berat_badan': int(row['berat_badan']) if pd.notna(row['berat_badan']) else 0,
                        'gol_darah': row['gol_darah'],
                        'pendidikan': row['pendidikan'],
                        'tgl_rekrut': self.parse_date(row['tgl_rekrut']),
                        'status_karyawan': row['status_karyawan'],
                        'tgl_kartetap': self.parse_date(row['tgl_kartetap']) if pd.notna(row['tgl_kartetap']) else None,
                        'jabatan': row['jabatan'],
                        'dept': row['dept'],
                        'kontrak_ke': int(row['kontrak_ke']) if pd.notna(row['kontrak_ke']) else 1,
                        'kontrak_berakhir': self.parse_date(row['kontrak_berakhir']) if pd.notna(row['kontrak_berakhir']) else None,
                        'no_rek_bank': str(row['no_rek_bank']),
                        'kode_bank': row['kode_bank'],
                        'nama_bank': row['nama_bank'],
                        'bpjs_tk': row['bpjs_tk'] == 'Ya',
                        'bpjs_tk_no': str(row['bpjs_tk_no']) if pd.notna(row['bpjs_tk_no']) else '',
                        'bpjs_kes': row['bpjs_kes'] == 'Ya',
                        'bpjs_kes_no': str(row['bpjs_kes_no']) if pd.notna(row['bpjs_kes_no']) else '',
                        'no_npwp': str(row['no_npwp']) if pd.notna(row['no_npwp']) else '',
                        'status_kerja': row['status_kerja'] != 'Keluar',
                        'tgl_out': self.parse_date(row['tgl_out']) if pd.notna(row['tgl_out']) else None,
                    }
                )
                success += 1
                self.stdout.write(f"✓ {success}: {row['nama']}")
                
            except Exception as e:
                failed += 1
                self.stdout.write(self.style.ERROR(f"✗ {row['nama']}: {str(e)}"))
        
        self.stdout.write(self.style.SUCCESS(f"\nSelesai! {success} berhasil, {failed} gagal"))
    
    def parse_date(self, value):
        if pd.isna(value):
            return None
        if isinstance(value, datetime):
            return value.date()
        return datetime.strptime(str(value), '%Y-%m-%d').date()