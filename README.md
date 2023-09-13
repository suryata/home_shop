# **Tugas 2 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

**Link Project**:[ HomeShop](https://home-shop.adaptable.app)

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Bonus: Kamu akan mendapatkan nilai bonus pada penilaian tugas ini apabila kamu berhasil mengimplementasikan dan mendemonstrasikan testing dasar selain testing yang diajarkan di tutorial.

# **Membuat sebuah proyek Django baru**
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
7. Lalu buka `settings.py` pada project yang kamu buat dan pada bagian `ALLOWED_HOSTS` tambahkan `*` agar semua host diizinkan untuk mengakses web milikmu.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Jalankan server Django dengan perintah `python manage.py runserver` (Windows) atau `./manage.py runserver` (Unix).
9. Buka http://localhost:8000 pada web untuk melihat animasi roket sebagai tanda aplikasi Django telah berhasil dibuat.
10. Untuk menghentikan server, tekan Ctrl+C (Windows/Linux) atau Control+C (Mac) pada shell.
11. Matikan *virtual environtment* dengan perintah `deactivate`

# *Membuat aplikasi dengan nama main pada proyek*
1. Jalankan perintah `python manage.py startapp main` di terminal atau *command prompt* yang dibuka dari direktori proyek yang sudah dibuat. 
2. Buka `settings.py` untuk menambahkan ``main`` ke dalam daftar aplikasi pada bagian *INSTALLED_APPS*.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

# *Melakukan routing pada proyek agar dapat menjalankan aplikasi main*
1. Buka berkas urls.py pada direktori proyek
2. Impor fungsi include dari django.urls seperti ini:
   ```
   from django.urls import path, include
   ```
3. Kemudian tambahkan path dari aplikasi main kedalam urlpatterns milik proyek
   ```python
   urlpatterns = [
   ...
    path('main/', include('main.urls')),
   ...
]```


# *Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib*
1. Buka berkas models.py pada direktori aplikasi main
2. Isi berkas models.py dengan class Item dengan atribut yang diinginkan, contohnya:
```python
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
```
**Penjelasan Kode:**
* `name` sebagai nama item yang tipenya `CharField`.
* `amount` sebagai jumlah item tipenya `IntegerField`.
* `description` sebagai deskripsi item yang tipenya `TextField`.
* `price` sebagai harga item tipenya `IntegerField`.
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi pada Django.

# *Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu*  
1. Buka berkas views.py yang terletak di dalam berkas aplikasi main.
2. Tambahkan baris impor berikut di bagian paling atas: 'from django.shortcuts import render'
3. Tambahkan fungsi 'show_main' di bawah impor:
   ```python
   def show_main(request):
    context = {
        'app_name':'Home Shop',
        'name': 'I Made Surya Anahata Putra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
   ```
   **Penjelasan Kode:**
* Import berguna untuk mengimpor fungsi *render* dari modul `django.shortcuts` yang digunakan untuk memproses tampilan HTML dengan data yang ada.
* Fungsi `show_main` berfungsi untuk mengatur permintaan HTTP dan mengembalikan tampilan yang tepat.
* `context` digunakan sebagai dictionary data yang akan diinput kedalam berkas main.html.
* `return render(request, "main.html", context)` digunakan untuk melakukan *rendering* tampilan `main.html` dengan menggunakan fungsi `render`yang memiliki argumen `request` sebagai objek permintaan HTTP dari *user*.
  
4.  Buatlah direktori templates pada direktori main dan tambahkan berkas main.html
5.  Modifikasi template main.html pada direktori templates yang ada pada main, contohnya:
   ```
<html>
<head>
    <title>{{app_name}}</title>
</head>
<body>
    <h1>Selamat Datang di {{app_name}}</h1>
    <h2>The best Shop in town</h2>
    <h5>App Name:</h5>
    <p>{{app_name}}</p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    <ul>
        <li><a href="/" title="">home</a></li>
        <li><a href="/main/" title="">main</a></li>
    </ul> 
</body>
</html>
```
**Penjelasan Kode:**
* sintaks `{{...}}` digunakan untuk menampilkan data yang telah diberikan sesuai dictionary di `context`.
* kode diatas hanya menampilkan nama aplikasi, nama, dan kelas dalam context yang diminta.

# *Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py*

1.Buatlah berkas urls.py di dalam direktori main
2. Isi urls.py dengan kode:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

**Penjelasan Kode:**
* pada kode tersebut saya membuat path dari urls.py yang terdapat dalam berkas main ke views.py yang ada pada berkas main
* kode tersebut akan memetakan fungsi show_main yang terdapat dalam berkas views.py yang sudah dibuat sebelumnya

# *Membuat akun dan *Deploy* di Adaptable.io*
1. Buat akun [Adaptable.io](https://adaptable.io/) menggunakan akun Github yang digunakan untuk membuat proyek.
2. Tekan tombol `New App` dan pilih `Connect an Existing Repository`.
3. Hubungkan Adaptable.io dengan Github dengan memilih `All Repository` pada saat instalasi dan pilih repositori proyekyang dibuat sebagai basisnya. Pilih *branch* yang ingin dijadikan *deployment branch*
4. Pilihlah `Python App Template` sebagai *template*
5. Pilih `PostgreSQL` sebagai basis data.
6. Pilih versi Python yang sesuai dan pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn <NAMA_PROYEK>.wsgi`.
7. Masukkan nama aplikasi yang akan jadi nama *domain* situs webmu.
8. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *Deployment* aplikasi.

# *Membuat dan mengunggah proyek ke Github*
1. Di dalam direktori yang sudah dibuat, buka *command prompt* (Windows) atau *terminal shell* (Unix). Lalu inisiasi repositori baru dengan perintah `git init`.
2. Lakukan konfigurasi *username* dengan perintah `git config user.name "<NAME>"` dan *email* dengan perintah `git config user.email "<EMAIL>"` yang akan dihubungkan dengan proyekmu ke repositori Git. (*username* dan *email* disesuaikan dengan Github mu). Lalu pastikan informasi itu sudah berubah dengan menjalankan perintah `git config --list --local`.
3. Buka akun [Github](https://github.com/) yang akan digunakan, dan buat repositori baru dengan nama yang diinginkan (Contoh yang saya gunakan adalah `goodang_project`). Atur visibilitas menjadi *Public* dan biarkan yang lainnya sesuai *default* nya.
4. Pilih direktori lokal yang sudah diinisiasi Git, di terminal atau *command prompt* jalankan perintah `git branch -M main` untuk membuat branch utama dengan nama "main".
5. Jalankan perintah `git remote add origin <URL_REPO>` untuk menghubungkan direktori lokal dengan repositori di Github. (Gannti URL_REPO dengan URL HTTPS di direktori Github yang sudah dibuat).
6. Buat berkas `.gitignore` di direktori lokal dan diisi dengan teks berikut. (Berkas ini berfungsi untuk mengabaikan beberapa berkas oleh Git)
```.gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```
7. Untuk melakukan penyimpanan pembaruan dapat melakukan `add`, `commit`, dan `push` dari terminal atau *command prompt* yang dibuka dari direktori lokal.







