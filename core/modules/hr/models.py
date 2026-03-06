import uuid
from django.db import models

class Employee(models.Model):
    # === IDENTITAS DASAR (WAJIB) ===
    nik = models.CharField(max_length=8, unique=True)  # WAJIB
    nama = models.CharField(max_length=100)  # WAJIB
    sex = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)  # sementara ga WAJIB
    tempat_lahir = models.CharField(max_length=50, blank=True, null=True)
    
    # === KONTAK & ALAMAT (OPSIONAL) ===
    no_hp = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    kelurahan = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    kabupaten_kota = models.CharField(max_length=50, blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    kode_pos = models.CharField(max_length=10, blank=True, null=True)
    
    # === DOKUMEN (OPSIONAL) ===
    # no_ktp = models.CharField(max_length=16, unique=True, blank=True, null=True)
    no_ktp = models.CharField(max_length=16, blank=True, null=True)
    no_kk = models.CharField(max_length=16, blank=True, null=True)
    
    # === STATUS (OPSIONAL) ===
    status_kawin = models.CharField(max_length=20, choices=[
        ('TK', 'Tidak Kawin'), 
        ('K0', 'Kawin 0'), 
        ('K1', 'Kawin 1'), 
        ('K2', 'Kawin 2'), 
        ('K3', 'Kawin 3')
    ], blank=True, null=True)
    tanggungan = models.IntegerField(default=0, blank=True, null=True)
    agama = models.CharField(max_length=20, blank=True, null=True)
    
    # === FISIK (OPSIONAL) ===
    tinggi_badan = models.IntegerField(blank=True, null=True, help_text="dalam cm")
    berat_badan = models.IntegerField(blank=True, null=True, help_text="dalam kg")
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    
    # === PENDIDIKAN & PEKERJAAN ===
    pendidikan = models.CharField(max_length=20, blank=True, null=True)
    tgl_rekrut = models.DateField()  # WAJIB
    status_karyawan = models.CharField(max_length=20, choices=[
        ('Tetap', 'Tetap'), 
        ('Kontrak', 'Kontrak'), 
        ('Probation', 'Probation'), 
        ('Outsourcing', 'Outsourcing')
    ])  # WAJIB
    tgl_kartetap = models.DateField(blank=True, null=True)
    
    # === POSISI (WAJIB) ===
    dept = models.CharField(max_length=50)  # WAJIB
    jabatan = models.CharField(max_length=50)  # WAJIB
    posisi_karyawan = models.CharField(max_length=50, blank=True, null=True)
    
    # === KONTRAK (OPSIONAL) ===
    kontrak_ke = models.IntegerField(default=1, blank=True, null=True)
    kontrak_berakhir = models.DateField(blank=True, null=True)
    
    # === BANK & GAJI (OPSIONAL) ===
    kode_gaji = models.CharField(max_length=20, blank=True, null=True)
    no_rek_bank = models.CharField(max_length=20, blank=True, null=True)
    kode_bank = models.CharField(max_length=10, blank=True, null=True)
    nama_bank = models.CharField(max_length=50, blank=True, null=True)
    
    # === BPJS (OPSIONAL) ===
    bpjs_tk = models.BooleanField(default=False)
    bpjs_tk_no = models.CharField(max_length=20, blank=True, null=True)
    bpjs_kes = models.BooleanField(default=False)
    bpjs_kes_no = models.CharField(max_length=20, blank=True, null=True)
    
    # === PAJAK (OPSIONAL) ===
    status_ptkp = models.CharField(max_length=20, blank=True, null=True)
    no_npwp = models.CharField(max_length=20, blank=True, null=True)
    status_pajak = models.CharField(max_length=20, blank=True, null=True)
    
    # === LAIN-LAIN (OPSIONAL) ===
    faskes = models.CharField(max_length=50, blank=True, null=True)
    placement = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='foto_karyawan/', blank=True, null=True)
    
    # === STATUS KELUAR (OPSIONAL) ===
    tgl_out = models.DateField(blank=True, null=True)
    status_kerja = models.BooleanField(default=True)
    
    # === IMPORT VERSIONING FIELDS ===
    import_batch = models.UUIDField(default=uuid.uuid4, editable=False)
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    imported_at = models.DateTimeField(auto_now_add=True)
    
    # === TIMESTAMPS ===
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nik} - {self.nama}"