##**Tugas 2 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

**Link Project: ** [HomeShop](https://home-shop.adaptable.app).

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Bonus: Kamu akan mendapatkan nilai bonus pada penilaian tugas ini apabila kamu berhasil mengimplementasikan dan mendemonstrasikan testing dasar selain testing yang diajarkan di tutorial.

##**Membuat sebuah proyek Django baru**
1. Buat direktori baru dengan nama yang diinginkan, contohnya 'projectbaru'. Kemudian buka command prompt (Windows) atau terminal shell (Unix) dan masuk kedalam direktori tersebut.
2. Buat *virtual environment* untuk mengisolasi proyek kita dengan perintah `python -m venv env`.
3. Kemudian aktifkan *virtual environment* dengan perintah `env\Scripts\activate.bat` untuk Windows dan `source env/bin/activate` untuk Unix (Mac/Linux).
   **NOTE:** Jika *virtual environment* sudah aktif akan ditandai dengan `(env)` di baris input terminal
4. Buat berkas dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa *dependencies* ke dalamnya.
   ```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Jalankan *virtual environment* terlebih dahuku dan jalankan perintah `pip install -r requirements.txt` pada command prompt.
6. Buat proyek Django dengan nama yang kamu inginkan dengan perintah `django-admin startproject namaproject .`


