# **Tugas 4 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

## **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
`UserCreationForm` dalam Django adalah sebuah formulir bawaan yang disediakan oleh kerangka kerja Django untuk memudahkan proses pendaftaran pengguna dalam aplikasi web. Form ini telah dirancang khusus untuk mencakup bidang seperti nama pengguna, kata sandi, dan konfirmasi kata sandi. Kelebihan utamanya adalah kemudahannya dalam penggunaan dan integrasinya yang lancar dengan model pengguna bawaan Django. Form ini juga mencakup validasi otomatis untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan persyaratan yang ditetapkan. Selain itu, penggunaan UserCreationForm dapat menghemat waktu pengembangan karena pengembang tidak perlu membuat formulir pendaftaran dari awal. Namun, perlu diperhatikan bahwa dalam beberapa situasi,perlu adanya tampilan atau logika tambahan sesuai dengan kebutuhan khusus aplikasi, karena form ini mungkin memiliki keterbatasan dalam hal kustomisasi dan tampilan yang sangat spesifik.
Kelebihan utama dari UserCreationForm adalah:
+ Kemudahan Penggunaan
Form ini sudah tersedia dan siap digunakan dengan konfigurasi standar. Anda dapat menggunakannya dengan mudah tanpa perlu membuat formulir pendaftaran dari awal.
+ Validasi Terintegrasi
Form ini memiliki validasi bawaan yang membantu memastikan kebenaran data yang dimasukkan oleh pengguna, seperti memastikan kata sandi cocok dengan konfirmasi kata sandi.
+ Integrasi Model User
Form ini bekerja dengan model pengguna bawaan Django (User) dengan baik, sehingga ketika data dimasukkan dan disubmit, akun pengguna baru akan dibuat dan disimpan di database secara otomatis.
## **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
## **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
## **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar<br>
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal<br>
- [x] Menghubungkan model Item dengan User<br>
- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi<br>
## ** Melakukan add-commit-push ke GitHub**


# **Tugas 3 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>
## **Apa perbedaan antara form POST dan form GET dalam Django?**
Form POST dan form GET dalam Django adalah dua metode yang berbeda yang digunakan untuk mengirim data dari formulir HTML ke server, dan mereka memiliki perbedaan signifikan dari berbagai sudut pandang.

+ Form POST digunakan ketika data yang dikirimkan dari formulir harus diproses oleh server. Metode ini memiliki tujuan utama untuk mengirim data kepada server agar dapat diolah lebih lanjut. Ini adalah pilihan yang paling umum digunakan ketika kita ingin menyimpan, memperbarui, atau melakukan tindakan tertentu berdasarkan data yang diberikan oleh pengguna. Data yang dikirim melalui form POST tidak terlihat dalam URL, sehingga menjadikannya pilihan yang lebih aman untuk mengirim data sensitif, seperti kata sandi atau informasi pribadi. Data dalam form POST disampaikan dalam tubuh permintaan HTTP.

+ Sebaliknya, form GET digunakan ketika kita ingin mengambil data dari server tanpa mempengaruhi status atau data di server. Tujuan utamanya adalah untuk mengirim permintaan dengan parameter-parameter yang disertakan dalam URL untuk mendapatkan hasil atau informasi yang relevan dari server. Form GET sering digunakan untuk pencarian atau tindakan baca, di mana data yang dikirim dengan form GET muncul dalam query string URL. Ini membuat data terlihat dalam URL dan dapat diakses oleh pengguna atau pihak ketiga yang melihat URL. Oleh karena itu, form GET tidak cocok untuk mengirim data sensitif.

+ Selain itu, perbedaan lain antara keduanya adalah dalam hal batasan panjang data. Form POST tidak memiliki batasan panjang data yang ketat, sehingga dapat digunakan untuk mengirim data yang lebih besar, sementara form GET memiliki batasan panjang URL yang dapat bervariasi antara browser dan server, yang dapat mengakibatkan masalah jika data terlalu besar.

+ Terakhir, dari segi caching dan bookmarking, permintaan POST tidak dapat di-cache oleh browser atau server proxy, dan URL tidak dapat dengan mudah dibookmark atau dibagikan oleh pengguna karena data tidak muncul dalam URL. Sementara itu, permintaan GET dapat di-cache oleh browser dan server proxy, yang memungkinkan pengguna untuk menciptakan tautan yang mengakses halaman dengan parameter yang sudah ditentukan. Pilihan antara form POST dan form GET harus didasarkan pada kebutuhan aplikasi kita. Form POST lebih sesuai untuk pengiriman data sensitif atau data yang mungkin besar, sedangkan form GET lebih cocok untuk permintaan yang bersifat idempoten (tidak mengubah status sumber daya) atau ketika kita ingin data tersedia dalam URL untuk berbagi atau penyimpanan bookmark. 

## **Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
Perbedaan utama antara XML (eXtensible Markup Language), JSON (JavaScript Object Notation), dan HTML (HyperText Markup Language) dalam konteks pengiriman data adalah sebagai berikut:

1. Tujuan Utama
+ XML dirancang untuk menggambarkan struktur data dan tujuannya adalah untuk pertukaran data antara aplikasi yang berbeda. Ini adalah format yang sangat fleksibel dan sering digunakan dalam berbagai aplikasi.
+ JSON lebih fokus pada representasi data dalam bentuk objek dan array, dan digunakan secara luas untuk pertukaran data antar aplikasi, terutama dalam pengembangan web dan RESTful APIs.
+ HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Tujuan utamanya adalah untuk menampilkan data secara terstruktur dalam bentuk yang dapat dibaca oleh manusia dalam browser web.

2. Notasi
+ XML menggunakan notasi markup dengan tag dan atribut. Ini memiliki struktur yang lebih rinci dan lebih banyak karakter, yang membuatnya lebih sulit dibaca oleh manusia.
+ JSON menggunakan notasi objek dan array yang sangat mirip dengan struktur data dalam bahasa pemrograman. Ini membuatnya lebih mudah dibaca dan dimengerti oleh manusia.
+ HTML juga menggunakan notasi markup dengan tag dan atribut, tetapi notasi ini dikhususkan untuk memformat konten web.

3. Sintaks
+ XML memiliki sintaksis yang lebih ketat dan memerlukan tag pembuka dan penutup yang sesuai. Ini dapat membuat dokumen XML lebih berat secara visual.
+ JSON memiliki sintaksis yang lebih ringan dan sederhana. Data disusun dalam pasangan "kunci-nilai" dan dapat diatur dalam bentuk objek dan array.
+ HTML memiliki sintaksis yang khusus untuk membangun elemen-elemen struktural dalam halaman web, seperti heading, paragraf, daftar, dll.

4. Pemrosesan:
+ XML memiliki dukungan yang kuat untuk skema, validasi, dan pemrosesan yang kompleks. Ini bisa menjadi pilihan yang baik untuk data yang memerlukan validasi ketat atau pemodelan data yang kompleks.
+ JSON adalah format yang lebih sederhana dan cenderung lebih mudah diproses oleh bahasa pemrograman. Ini adalah pilihan yang baik untuk pertukaran data antar aplikasi dan API.
+ HTML digunakan untuk membuat tampilan konten web dalam browser, dan biasanya diolah oleh browser secara otomatis.

## **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki sejumlah keunggulan, yaitu:
+ Sintaks yang Sederhana
  JSON memiliki sintaks yang sangat sederhana yang membuatnya mudah dipahami oleh manusia. Data dalam JSON diatur dalam pasangan "kunci-nilai" yang sangat mirip dengan struktur data dalam bahasa pemrograman. Ini menjadikannya format yang intuitif dan mudah dibaca.
+ Dukungan Lintas Bahasa
  JSON tidak terbatas pada bahasa pemrograman tertentu. Hampir semua bahasa pemrograman modern memiliki dukungan untuk memparsing (membaca) dan menghasilkan (menghasilkan) data dalam format JSON. Ini menjadikannya format yang sangat serbaguna untuk pertukaran data antar aplikasi yang ditulis dalam berbagai bahasa.
+ Ringan dan Efisien
  JSON adalah format yang ringan dan memiliki overhead yang relatif kecil, sehingga cocok untuk pertukaran data di lingkungan jaringan, terutama di lingkungan web yang memiliki lalu lintas data yang tinggi.
+ Fleksibel
  Hal ini karena JSON dapat menyimpan beragam struktur data seperti objek, array, string, dan tipe data lainnya yang sering dipakai.
  
## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.<br>
+ Pada direktori `main` buat berkas baru `forms.py`. Lalu isilah dengan kode dibawah ini
```
  from django.forms import ModelForm
  from main.models import Item
  
  class ItemForm(ModelForm):
      class Meta:
          model = Item
          fields = ["name", "price", "description","amount"]
```
+ Buka berkas `views.py` pada direktori `main` dan tambahkan beberapa import
```
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```
+ Lalu pada file yang sama, buatlah fungsi baru bernama `create_product` dengan parameter `request` seperti dibawah ini
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
+ Ubah fungsi `show_main` yang sudah ada pada berkas `views.py` menjadi seperti berikut 
```
def show_main(request):
    products = Item.objects.all()
    total_item = 0
    for i in products:
        total_item += 1
    context = {
        'app_name':'Home Shop',
        'name': 'I Made Surya Anahata Putra',
        'class': 'PBP A',
        'products': products,
        'total_item': total_item
    }

    return render(request, "main.html", context)
```
+ Buka `urls.py` pada direktori `main` dan import fungsi `create_product`
```
from main.views import show_main, create_product
```
+ Tambahkan path url ke dalam `urlpatterns` pada `urls.py` di `main`
```
path('create-product', create_product, name='create_product'),
```
+ Buat berkas HTML baru dengan nama `create_product.html` pada direktori `main/templates`. Isi `create_product.html` dengan kode berikut:
  ```
     {% extends 'base.html' %} 
   
   {% block content %}
   <h1>Add New Product</h1>
   
   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>
   
   {% endblock %}
   ```
+ Buka `main.html` dan tambahkan kode berikut di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk table serta tombol "Add New Product" yang akan redirect ke halaman form.
  ```
      <div class="table-container">    
        <table class="table table-bordered">
            <thead class="table-secondary">
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Description</th>
                    <th>Amount</th>
                    <th>Date Added</th>
                </tr>
            </thead>

            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

            {% for Item in products %}
                <tr>
                    <td>{{Item.name}}</td>
                    <td>{{Item.price}}</td>
                    <td>{{Item.description}}</td>
                    <td>{{Item.amount}}</td>
                    <td>{{Item.date_added}}</td>
                </tr>
            {% endfor %}
        </table>

        <a href="{% url 'main:create_product' %}">
            <button>
                Add New Product
            </button>
        </a>
    </div>
  ```
- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. <br>
__Fungsi `views` untuk formal HTML__
+ Pada`views.py` lengkapi fungsi `show_main` untuk melihat dalam format HTML dengan menambahkan beberapa kode menjadi seperti dibawah ini 
```python
def show_main(request):
    products = Item.objects.all()
    total_item = 0
    for i in products:
        total_item += 1
    context = {
        'app_name':'Home Shop',
        'name': 'I Made Surya Anahata Putra',
        'class': 'PBP A',
        'products': products,
        'total_item': total_item
    }

    return render(request, "main.html", context)
```

__Fungsi `views` untuk format XML__
+ Buka `views.py` pada direktori `main` dan tambahkan import `HttpResponse` dan `Serializer`.
```
from django.http import HttpResponse
from django.core import serializers
```
+ Buat fungsi `show_xml` yang menerima parameter request dan buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items serta tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil `query` yang sudah diserialisasi menjadi format XML dan parameter `content_type="application/xml"`.
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
+ Buka `urls.py` yang ada pada folder main dan import fungsi yang sudah dibuat
```
from main.views import show_main, create_product, show_xml 
```
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi
  ```
    ...
    path('xml/', show_xml, name='show_xml'), 
    ...
  ```
__Fungsi `views` untuk format JSON__
+ Pada berkas `views.py` pada direktori `main`, buat fungsi `show_json` yang menerima parameter request dan buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items serta tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil `query` yang sudah diserialisasi menjadi format JSON dan parameter `content_type="application/json"`.
```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
+ Buka `urls.py` yang ada pada folder main dan import fungsi yang sudah dibuat
```
from main.views import show_main, create_product, show_xml, show_json
```
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi
  ```
    ...
    path('json/', show_json, name='show_json'),  
    ...
  ```
__Fungsi `views` untuk format XML by ID dan JSON by ID__
+ Buka berkas `views.py` pada direktori `main` dan buatlah fungsi baru yang menerima parameter request dan id dengan nama `show_xml_by_id` dan `show_json_by_id`. Lalu buat sebuah variable untuk menyimpan hasil query dari seluruh data yang ada pada Items. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type` dengan value `"application/xml"` (untuk format XML) atau `"application/json"` (untuk format JSON).
+ XML
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
+ JSON
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
+ Buka `urls.py` yang ada pada folder main dan import fungsi yang sudah dibuat
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi
  ```
    ...
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
    ...
  ```
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2. <br>
+ Buka berkas `urls.py` pada direktori `main` dan import fungsi yang sudah dibuat
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
+ Tambahkan beberapa path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport

```
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```


## **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md**
__Dokumentasi Akses URL HTML__
![HTML](https://cdn.discordapp.com/attachments/1037716635227799613/1153736811974230157/image.png)
![HTML](https://cdn.discordapp.com/attachments/1037716635227799613/1153737564050686043/image.png)
__Dokumentasi Akses URL XML__
![XML](https://cdn.discordapp.com/attachments/1037716635227799613/1153736121600184340/image.png)
__Dokumentasi Akses URL JSON__
![JSON](https://cdn.discordapp.com/attachments/1037716635227799613/1153736060313022504/image.png)
__Dokumentasi Akses URL XML by ID__
![XML by ID](https://cdn.discordapp.com/attachments/1037716635227799613/1153736323606253730/image.png)
__Dokumentasi Akses URL JSON by ID__
![JSON by ID](https://cdn.discordapp.com/attachments/1037716635227799613/1153736401720967299/image.png)
## **Melakukan add-commit-push ke GitHub**

# **Tugas 2 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

**Link Project**:[ HomeShop](https://home-shop.adaptable.app)

## **1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
   
## **Membuat sebuah proyek Django baru**
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

## **Membuat aplikasi dengan nama main pada proyek**
1. Jalankan perintah `python manage.py startapp main` di terminal atau *command prompt* yang dibuka dari direktori proyek yang sudah dibuat. 
2. Buka `settings.py` untuk menambahkan ``main`` ke dalam daftar aplikasi pada bagian *INSTALLED_APPS*.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

## **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
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
   ]
   ```

## **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib**
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

## **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**  
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
   ```html
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

## **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**

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

## **Membuat akun dan *Deploy* di Adaptable.io**
1. Buat akun [Adaptable.io](https://adaptable.io/) menggunakan akun Github yang digunakan untuk membuat proyek.
2. Tekan tombol `New App` dan pilih `Connect an Existing Repository`.
3. Hubungkan Adaptable.io dengan Github dengan memilih `All Repository` pada saat instalasi dan pilih repositori proyekyang dibuat sebagai basisnya. Pilih *branch* yang ingin dijadikan *deployment branch*
4. Pilihlah `Python App Template` sebagai *template*
5. Pilih `PostgreSQL` sebagai basis data.
6. Pilih versi Python yang sesuai dan pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn <NAMA_PROYEK>.wsgi`.
7. Masukkan nama aplikasi yang akan jadi nama *domain* situs webmu.
8. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *Deployment* aplikasi.

## **Membuat dan mengunggah proyek ke Github**
1. Di dalam direktori yang sudah dibuat, buka *command prompt* (Windows) atau *terminal shell* (Unix). Lalu inisiasi repositori baru dengan perintah `git init`.
2. Lakukan konfigurasi *username* dengan perintah `git config user.name "<NAME>"` dan *email* dengan perintah `git config user.email "<EMAIL>"` yang akan dihubungkan dengan proyekmu ke repositori Git. (*username* dan *email* disesuaikan dengan Github mu). Lalu pastikan informasi itu sudah berubah dengan menjalankan perintah `git config --list --local`.
3. Buka akun [Github](https://github.com/) yang akan digunakan, dan buat repositori baru dengan nama yang diinginkan. Atur visibilitas menjadi *Public* dan biarkan yang lainnya sesuai *default* nya.
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

## **2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**
   
## **Bagan *request* dan *response client* dengan Django**
![bagan](https://cdn.discordapp.com/attachments/1037716635227799613/1151366728345993226/image0.jpg)
**Penjelasan**
* *User*/pengguna mengakses website dan melakukan *HTTP request*
* *Request* yang masuk diteruskan ke `urls.py` dan akan melakukan proses pencarian terhadap *pattern* url yang sesuai.
* Setelah ditemukan, Django akan memanggil fungsi yang sesuai pada `views.py`, *logic handling* mengenai database dan mengakses template yang sesuai akan dilakukan disini. Data dari database dapat diakses dan diproses sesuai *logic* dari `models.py`.
* *Database* adalah tempat dimana data aplikasi disimpan, dimana data disini dapat diubah sengan perintah dari `models.py`.
* *Template* disini berfungsi untuk mengatur tampilan halaman web yang akan dikembalikan ke *user*
* Kemudian setelah *logic handle* pada views.py selesai maka akan menampilkan tampilan yang sesuai ke user berupa HTTP response

## **3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment adalah lingkungan yang terisolasi yang digunakan oleh pengembang perangkat lunak untuk mengelola dependensi dan paket yang dibutuhkan oleh proyek mereka. Kita menggunakan *virtual environment* untuk mengisolasi lingkungan kerja kita dari lingkungan kerja lainnya. Dengan virtual environment, kita dapat menginstal versi Python dan modul yang berbeda untuk setiap proyek yang kita kerjakan. Hal ini dapat mencegah terjadinya konflik antar proyek, karena masing-masing proyek memiliki lingkungannya sendiri.

Tanpa menggunakan *virtual environment* sebetulnya kita tetap bisa membuat aplikasi web berbasis Django. Namun hal ini tidak disarankan karena dapat menyebabkan bentroknya package serta dependencies yang berbeda versi dengan yang sudah ada di perangkat kita. Selain itu, dalam berbagi proyek dengan orang lain menjadi lebih sulit karena mereka mungkin memiliki versi Django atau paket lain yang berbeda di sistem mereka. Maka dari itu, disarankan untuk mengaktifkan virtual environment untuk menghindari hal-hal tersebut dan membuat pengembangan web berbasis Django lebih efektif.

## **4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya**
MVC(Model—View—Controller), MVT(Model View Template), dan MVVM(Model — View — ViewModel ) adalah tiga pola desain perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen aplikasi dan meningkatkan pemahaman, pemeliharaan, serta skalabilitas kode.

1. MVC (Model-View-Controller):

Model: Bertanggung jawab untuk mengelola data dan logika dalam aplikasi. Ini adalah komponen yang merepresentasikan struktur data aplikasi dan berurusan dengan perubahan data dan validasi.
View: Menampilkan informasi kepada pengguna dan menangani tampilan grafis atau antarmuka pengguna (UI). Ini menerima input dari pengguna dan mengirimkannya ke Controller.
Controller: Bertindak sebagai perantara antara Model dan View. Ini mengambil input dari pengguna, memprosesnya, berkomunikasi dengan Model untuk mendapatkan atau memodifikasi data, dan memperbarui View.

2. MVT (Model-View-Template):

Model: Serupa dengan MVC, Model mengelola logika dan data aplikasi.
View: Menampilkan informasi kepada pengguna, tetapi dalam konteks Django (framework Python untuk pengembangan web), View adalah komponen yang mengatur tampilan dan berfungsi sebagai penghubung antara Model dan Template.
Template: Ini adalah bagian yang mengatur tampilan atau presentasi data. Template menggunakan sintaks template khusus untuk mengambil data dari Model dan mempresentasikannya dalam HTML.
Perbedaan: MVT adalah varian dari MVC yang digunakan dalam Django. Dalam MVT, View berfungsi lebih seperti Controller dalam MVC, sementara Template menggantikan peran View dalam MVC.

3. MVVM (Model-View-ViewModel):

Model: Seperti dalam MVC dan MVT, Model mengelola logika bisnis dan data aplikasi.
View: Menampilkan informasi kepada pengguna. Dalam MVVM, View biasanya lebih pasif daripada dalam MVC atau MVT. Ini tidak memiliki logika bisnis dan hanya menampilkan apa yang diberikan oleh ViewModel.
ViewModel: Ini adalah komponen yang menghubungkan antara Model dan View. ViewModel mengubah data dari Model menjadi format yang dapat ditampilkan oleh View dan mengatur tindakan pengguna yang dapat mempengaruhi Model. ViewModel sering digunakan dalam aplikasi berbasis antarmuka pengguna (UI) yang kompleks dan dalam pengembangan aplikasi berbasis perangkat lunak modern.
Perbedaan: MVVM adalah pola desain yang umumnya digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama aplikasi berbasis perangkat lunak modern seperti aplikasi web yang menggunakan teknologi seperti React, Angular, atau Vue.js. 

**Perbedaan utama ketiganya:**

*MVC adalah pola desain umum yang memisahkan Model, View, dan Controller. Disini view bekerja menampilkan antarmuka pengguna dan Controller memproses input pengguna.

*MVT adalah variasi MVC yang digunakan dalam Django, dengan View yang mengambil peran Controller dan Template yang mengambil peran View.

*MVVM adalah pola desain yang digunakan dalam pengembangan antarmuka pengguna modern, dengan ViewModel yang menghubungkan antara Model dan View. Disini view yang bekerja menampilkan antarmuka pengguna dan ViewModel yang memproses input pengguna.



