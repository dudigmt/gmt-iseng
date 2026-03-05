from django.db import models

class Employee(models.Model):
    # Identitas Dasar
    nik = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    tgl_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=50)
    
    # Kontak & Alamat
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    kelurahan = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kabupaten_kota = models.CharField(max_length=50)
    provinsi = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=10)
    
    # Dokumen
    no_ktp = models.CharField(max_length=16, unique=True)
    no_kk = models.CharField(max_length=16)
    
    # Status
    status_kawin = models.CharField(max_length=20, choices=[('TK', 'Tidak Kawin'), ('K0', 'Kawin 0'), ('K1', 'Kawin 1'), ('K2', 'Kawin 2'), ('K3', 'Kawin 3')])
    tanggungan = models.IntegerField(default=0)
    agama = models.CharField(max_length=20)
    
    # Fisik
    tinggi_badan = models.IntegerField(help_text="dalam cm")
    berat_badan = models.IntegerField(help_text="dalam kg")
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    
    # Pendidikan & Pekerjaan
    pendidikan = models.CharField(max_length=20)
    tgl_rekrut = models.DateField()
    status_karyawan = models.CharField(max_length=20, choices=[('Tetap', 'Tetap'), ('Kontrak', 'Kontrak'), ('Probation', 'Probation'), ('Outsourcing', 'Outsourcing')])
    tgl_kartetap = models.DateField(blank=True, null=True)
    
    # Posisi
    dept = models.CharField(max_length=50)  # atau foreign key nanti
    jabatan = models.CharField(max_length=50)
    posisi_karyawan = models.CharField(max_length=50)
    
    # Kontrak
    kontrak_ke = models.IntegerField(default=1)
    kontrak_berakhir = models.DateField(blank=True, null=True)
    
    # Bank & Gaji
    kode_gaji = models.CharField(max_length=20, blank=True, null=True)
    no_rek_bank = models.CharField(max_length=20)
    kode_bank = models.CharField(max_length=10)
    nama_bank = models.CharField(max_length=50)
    
    # BPJS
    bpjs_tk = models.BooleanField(default=False)
    bpjs_tk_no = models.CharField(max_length=20, blank=True, null=True)
    bpjs_kes = models.BooleanField(default=False)
    bpjs_kes_no = models.CharField(max_length=20, blank=True, null=True)
    
    # Pajak
    status_ptkp = models.CharField(max_length=20, blank=True, null=True)
    no_npwp = models.CharField(max_length=20, blank=True, null=True)
    status_pajak = models.CharField(max_length=20, blank=True, null=True)
    
    # Lain-lain
    faskes = models.CharField(max_length=50, blank=True, null=True)
    placement = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='foto_karyawan/', blank=True, null=True)
    
    # Status Keluar
    tgl_out = models.DateField(blank=True, null=True)
    status_kerja = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nik} - {self.nama}"