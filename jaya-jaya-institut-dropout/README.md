# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan yang sudah berdiri sejak tahun 2000 memiliki reputasi yang sangat baik dan sudah mencetak banyak lulusan yang sukses. saat ini sedang menghadapi kesulitan dalam mengelola siswa, terlihat dari tingginya jumlah dropout. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Kita sebagai calon data scientist masa depan diminta untuk membuat sebuah sistem machine learning yang dapat mendeteksi siswa yang mungkin akan melakukan dropout, serta membuat sebuah business dashboard yang dapat digunakan oleh pihak Jaya Jaya Institut untuk memantau perkembangan siswa.

### Permasalahan Bisnis

Permasalahan bisnis yang akan diselesaikan melalui proyek ini antara lain:

1. Identifikasi siswa yang berpotensi melakukan dropout.
2. Memberikan bimbingan khusus kepada siswa yang berisiko dropout.
3. Memiliki sistem pemantauan perkembangan siswa untuk meningkatkan efektivitas pengelolaan.
4. Memiliki *interface* sederhana berbasis web untuk menggunakan sistem machine learning.

### Cakupan Proyek

Proyek ini akan mencakup beberapa tahapan sebagai berikut:

1. Pengumpulan dan pembersihan data dari dataset Jaya Jaya Institut.
2. Pengembangan model machine learning untuk mendeteksi siswa yang berpotensi melakukan dropout.
3. Pembuatan business dashboard untuk memantau perkembangan siswa.
4. Pembuatan *interface* sederhana berbasis web untuk menggunakan sistem machine learning.

### Persiapan

Sumber data: [Dataset Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:

1. Pastikan sudah menginstall [Anaconda](https://www.anaconda.com/products/individual) atau [Miniconda](https://docs.conda.io/en/latest/miniconda.html) di komputer Anda.
2. Buka terminal atau command prompt.
3. Buat environment baru dengan perintah `conda create -n jaya-jaya-maju-dropout python=3.9`.
4. Aktifkan environment dengan perintah `conda activate jaya-jaya-maju-dropout`.
5. Install library yang dibutuhkan dengan perintah `pip install pandas matplotlib seaborn jupyter sqlalchemy psycopg2 scikit-learn==1.2.2 joblib==1.3.1 tensorflow`.
6. Buka Jupyter Notebook dengan perintah `jupyter-notebook .`.
7. Siap mengerjakan proyek.

## Business Dashboard

- Dashboard telah dibuat untuk memantau faktor-faktor kunci yang berpotensi mempengaruhi *graduation rate*.
- Diharapkan dashboard dapat membantu pihak Jaya Jaya Institut dalam memantau perkembangan siswa.
- Username dashboard: `root@mail.com`
- Password dashboard: `root123`

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion

Berdasarkan analisis data yang telah dilakukan, dapat disimpulkan bahwa faktor-faktor seperti *Curricular_units_2nd_sem_approved*, *Curricular_units_1st_sem_approved*, *Curricular_units_2nd_sem_grade*, *Curricular_units_1st_sem_grade*, *Tuition_fees_up_to_date*, *Scholarship_holder*, *Application_mode*, *Gender*, *Debtor*, dan *Age_at_enrollment* mempengaruhi tingkat kelulusan (*Graduated*) mahasiswa di Jaya Jaya Institut dan berlaku sebaliknya, dengan dashboard, diharapkan dapat mempermudah pihak Jaya Jaya Institut dalam memantau perkembangan siswa, sehingga dapat mengurangi jumlah siswa yang melakukan dropout.

### Rekomendasi Action Items

Berdasarkan hasil proyek, berikut adalah beberapa rekomendasi action items:

1. Melakukan bimbingan khusus terhadap siswa yang berpotensi melakukan dropout.
2. Tinjau kembali program beasiswa dan pertimbangkan penyesuaian untuk meningkatkan motivasi siswa.
3. Melakukan survey secara berkala kepada siswa untuk mengetahui permasalahan yang sedang dialami siswa.
