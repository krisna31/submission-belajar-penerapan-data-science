# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Perusahaan Jaya Jaya Maju adalah sebuah perusahaan multinasional yang sudah berdiri sejak tahun 2000 hingga sekarang, memiliki hingga 1000 karyawan yang tersebar di seluruh penjuru negeri, saat ini sedang menghadapi kesulitan dalam mengelola karyawan, terlihat dari tingginya *attrition* rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) yang mencapai lebih dari 10%. Manajer departemen HR dengan bantuan data scientist berusaha mengidentifikasi faktor-faktor yang mempengaruhi *attrition* rate yang tinggi tersebut serta membuat business dashboard guna memantau faktor-faktor tersebut.

### Permasalahan Bisnis

1. *Attrition* Rate yang Tinggi: *Attrition* rate perusahaan melebihi 10%, berpotensi merugikan produktivitas dan kestabilan organisasi.
2. Business Dashboard: Dashboard untuk memantau faktor-faktor yang mempengaruhi *attrition* rate.

### Cakupan Proyek

1. Identifikasi Faktor-faktor yang mempengaruhi *Attrition* Rate.
2. Pembuatan Business Dashboard untuk memantau dan mengelola faktor-faktor yang diidentifikasi.
<!-- 3. Menyusun dokumentasi yang rapi sesuai dengan yang diinginkan. -->

### Persiapan

Sumber data: [Dataset Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

1. Pastikan sudah menginstall [Anaconda](https://www.anaconda.com/products/individual) atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html) di komputer Anda.
2. Buka terminal atau command prompt.
3. Buat environment baru dengan perintah `conda create -n jaya-jaya-maju-*attrition* python=3.9`.
4. Aktifkan environment dengan perintah `conda activate jaya-jaya-maju-*attrition*`.
5. Install library yang dibutuhkan dengan perintah `pip install pandas matplotlib seaborn jupyter sqlalchemy psycopg2 scikit-learn==1.2.2 joblib==1.3.1`.
6. Buka Jupyter Notebook dengan perintah `jupyter-notebook .`.
7. Siap mengerjakan proyek.

## Business Dashboard

- Dashboard telah dibuat untuk memantau faktor-faktor kunci yang berpotensi mempengaruhi *attrition* rate.
- Username dashboard: `root@mail.com`
- Password dashboard: `root123`

## Conclusion

<!-- Jelaskan konklusi dari proyek yang dikerjakan. -->
Berdasarkan analisis data yang telah dilakukan, dapat disimpulkan bahwa faktor-faktor seperti *Stock Option Level*, total tahun bekerja, usia karyawan, tingkat jabatan, pendapatan bulanan, masa kerja dengan manajer saat ini, dan masa kerja dalam peran saat ini mempengaruhi tingkat *attrition* karyawan, dengan menggunakan business dashboard, HR dapat dengan cepat dan efektif mengambil tindakan proaktif, seperti pengembangan program retensi atau peningkatan kepuasan kerja.

### Rekomendasi Action Items

1. Lakukan survei kepuasan pekerja secara rutin untuk memahami perasaan dan kebutuhan karyawan
2. Implementasikan program pengembangan karir untuk meningkatkan retensi karyawan.

### How to use prediction.py file

1. buka terminal
2. pastikan python sudah terinstall
3. jalankan `python prediction.py`
4. isi inputan sesuai yang diminta
5. setelah selesai hasil prediksi akan keluar
