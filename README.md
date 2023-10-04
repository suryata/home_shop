# **Tugas 5 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

## **Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya**
Berikut adalah manfaat dan waktu yang tepat untuk menggunakan setiap jenis element selector dalam CSS:<br>

+ Type Selector (Tag Selector):<br>
Manfaat: Mengaplikasikan gaya ke semua elemen dengan nama tag tertentu.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya umum ke semua elemen dengan tag yang sama.<br>

+ ID Selector:<br>
Manfaat: Mengaplikasikan gaya ke elemen dengan ID tertentu.<br>
Waktu yang Tepat: Ketika perlu memberikan gaya khusus ke elemen unik dengan ID tertentu.<br>

+ Class Selector:<br>
Manfaat: Mengaplikasikan gaya ke semua elemen dengan class tertentu.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya khusus ke grup elemen dengan class yang sama.<br>

+ Attribute Selector:<br>
Manfaat: Mengaplikasikan gaya ke elemen berdasarkan atribut dan nilai atributnya.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya ke elemen dengan atribut tertentu.<br>

+ Descendant Selector:<br>
Manfaat: Mengaplikasikan gaya ke elemen yang merupakan keturunan dari elemen lain.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya ke elemen yang berada di dalam elemen lain.<br>

+ Child Selector:<br>
Manfaat: Mengaplikasikan gaya ke elemen yang merupakan anak langsung dari elemen lain.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya hanya ke anak langsung dan bukan ke semua keturunan.<br>

+ Pseudo-class Selector:<br>
Manfaat: Mengaplikasikan gaya berdasarkan keadaan atau status elemen.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya berdasarkan keadaan tertentu seperti hover atau focus.<br>

+ Pseudo-element Selector:<br>
Manfaat: Mengaplikasikan gaya ke bagian tertentu dari elemen.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya ke bagian spesifik dari elemen seperti first line atau first letter.<br>

+ Grouping Selector:<br>
Manfaat: Mengelompokkan beberapa selector untuk menerapkan gaya yang sama.<br>
Waktu yang Tepat: Ketika beberapa selector memerlukan gaya yang sama, sehingga mengurangi redundansi kode.<br>

+ Universal Selector:<br>
Manfaat: Mengaplikasikan gaya ke semua elemen pada halaman.<br>
Waktu yang Tepat: Ketika ingin memberikan gaya ke semua elemen, tetapi perlu digunakan dengan hati-hati karena dapat mempengaruhi semua elemen di halaman.<br>

+ Combination of Selectors:<br>
Manfaat: Mengaplikasikan gaya dengan target yang lebih spesifik.<br>
Waktu yang Tepat: Ketika perlu menargetkan elemen dengan cara yang lebih spesifik dan presisi.<br>

## **Jelaskan HTML5 Tag yang kamu ketahui**
Berikut adalah beberapa tag HTML5 yang umum digunakan:

- [x] Struktur Dokumen:<br>
  + `<!DOCTYPE html>`: Mendefinisikan dokumen sebagai HTML5.
  + `<html>`: Elemen root dari dokumen HTML.
  + `<head>`: Berisi informasi meta tentang dokumen.
  + `<body>`: Berisi konten utama dari dokumen HTML.
- [x] Struktur Konten:<br>
  + `<header>`: Digunakan untuk header dokumen atau bagian.
  + `<nav>`: Digunakan untuk navigasi.
  + `<main>`: Berisi konten utama dari dokumen.
  + `<footer>`: Digunakan untuk footer dokumen atau bagian.
- [x] Konten Teks:<br>
  + `<h1>` hingga `<h6>`: Heading atau judul, dari level 1 (paling penting) hingga level 6 (paling tidak penting).
  + `<p>`: Paragraf.
  + `<span>`: Digunakan untuk mengelompokkan atau menerapkan gaya ke teks inline.
  + `<strong>`: Teks tebal.
  + `<em>`: Teks miring.
- [x] Form:<br>
  + `<form>`: Digunakan untuk membuat form.
  + `<input>`: Digunakan untuk membuat berbagai jenis input, seperti teks, checkbox, radio button, dll.
  + `<label>`: Label untuk elemen <input>.
  + `<textarea>`: Input teks multiline.
  + `<button>`: Tombol.
- [x] Konten Media:<br>
  + `<img>`: Gambar.
  + `<audio>`: Elemen audio.
  + `<video>`: Elemen video.
  + `<source>`: Digunakan dalam <audio> atau <video> untuk mendefinisikan sumber media.
- [x] Tabel:<br>
  + `<table>`: Tabel.
  + `<tr>`: Baris tabel.
  + `<td>`: Sel data tabel.
  + `<th>`: Sel header tabel.
  + `<thead>`: Grup header tabel.
  + `<tbody>`: Grup badan tabel.
  + `<tfoot>`: Grup footer tabel.
- [x] List:<br>
  + `<ul>`: Daftar tidak terurut.
  + `<ol>`: Daftar terurut.
  + `<li>`: Item daftar.
- [x] Link:
  + `<a>`: Hyperlink.
- [x] Lainnya:<br>
  + `<canvas>`: Digunakan untuk menggambar grafik dengan JavaScript.
  + `<svg>`: Digunakan untuk mendefinisikan grafik vektor berbasis XML.
    
## **Jelaskan perbedaan antara margin dan padding**
+ Margin:<br>
Definisi: Margin adalah ruang di luar batas elemen, yang berfungsi sebagai ruang kosong antara elemen dengan elemen lain di sekitarnya.<br>
Posisi: Berada di luar border elemen.<br>
Kegunaan: Margin sering digunakan untuk membuat jarak atau ruang antara elemen-elemen pada halaman, seperti antara dua paragraf, dua div, atau antara elemen dengan tepi browser.<br>
Transparansi: Margin selalu transparan; tidak dapat diberi warna atau background.<br>

+ Padding:<br>
Definisi: Padding adalah ruang di dalam batas elemen, antara border dan konten elemen itu sendiri.<br>
Posisi: Berada di dalam border elemen.<br>
Kegunaan: Padding digunakan untuk membuat ruang di dalam elemen, yang dapat membuat elemen terlihat lebih besar atau memberikan ruang bernafas untuk konten di dalam elemen.<br>
Warna: Padding akan mengambil warna background dari elemen tersebut.<br>

## **Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
**Tailwind CSS:**<br>

Utility-First: Tailwind adalah framework CSS utility-first, yang berarti ia menyediakan banyak class utility yang dapat digunakan untuk membangun desain tanpa meninggalkan HTML. Ini memungkinkan pengembang untuk membuat antarmuka dengan cepat tanpa harus menulis CSS kustom.<br><br>
Kustomisasi: Tailwind sangat fleksibel dan dapat dikustomisasi dengan mudah. Pengembang dapat menambahkan, mengubah, atau menghapus class utility sesuai kebutuhan.<br><br>
Tidak Ada Komponen Bawaan: Tidak menyediakan komponen UI bawaan seperti Bootstrap. Ini memberikan kebebasan penuh kepada pengembang untuk membuat komponen sesuai kebutuhan.<br><br>
Pendekatan Desain Atomik: Mengikuti prinsip desain atomik, di mana desain dibangun menggunakan class-class kecil yang masing-masing mengatur satu properti atau nilai.<br><br>

**Bootstrap:**<br>
Komponen UI Bawaan: Bootstrap menyediakan komponen UI yang telah dirancang dan siap pakai, seperti navigasi, modals, dan kartu, yang dapat membantu mempercepat proses pengembangan.<br><br>
Tematik: Bootstrap memungkinkan pengembang untuk dengan mudah mengubah tema dengan variabel dan kelas yang telah ditentukan.<br><br>
JavaScript Plugins: Menyediakan plugin JavaScript untuk beberapa komponen, seperti carousel dan tooltips, yang memungkinkan fungsionalitas tambahan.<br><br>
Grid System: Bootstrap memiliki sistem grid yang kuat dan responsif, yang memudahkan pengembang untuk membuat layout yang kompleks.<br><br>

**Kapan Menggunakan Tailwind:**<br>
Proyek Kustom: Tailwind cocok untuk proyek yang memerlukan desain kustom atau tidak ingin terlihat seperti template Bootstrap klasik.<br><br>
Pengembangan Cepat: Jika Anda mencari pengembangan yang cepat dengan menggunakan class utility tanpa menulis banyak CSS kustom.<br><br>
Kontrol Desain: Cocok untuk pengembang yang ingin kontrol penuh atas desain tanpa harus overwrite style bawaan framework.<br><br>

**Kapan Menggunakan Bootstrap:**<br>
Prototyping Cepat: Bootstrap adalah pilihan yang baik untuk prototyping cepat karena menyediakan banyak komponen siap pakai.<br><br>
Pengembang Pemula: Cocok untuk pengembang yang belum terlalu familiar dengan CSS dan desain, karena menyediakan solusi desain yang konsisten dan terdokumentasi dengan baik.<br><br>
Proyek Standar: Jika proyek Anda tidak memerlukan desain yang terlalu kustom atau unik, Bootstrap dapat menjadi pilihan yang efisien dan cepat.<br><br>

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
* Pada direktori templates, buka berkas base.html lalu tambahkan kode dibawah ini
```
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```

* Tambahkan juga Bootstrap CSS dan juga JS
```
        {% endblock meta %}
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    </head>
```

- [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin<br>
+ Pada bagian  `index.html`, `about.html`, serta `main.html` tambahkan navbar dengan kode dibawah ini:
  ```
      {%load static%}
    
    <link rel="stylesheet" type="text/css" href="{% static 'css/navstyle.css' %}">
    <nav class="navbar bg-white fixed-top navbar-expand-sm" id="myNav" >
        <div class="container-fluid">
          <a class="navbar-brand" href="/">
                <img src="{% static 'img/log.png' %}" alt="">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-  expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/" title="">HOME</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/main" title="">MAIN</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="/about" title="">ABOUT</a>
              </li>
            </ul>
          </div>
        </div>
    </nav>

  ```
+ Kemudian customisasi halaman `login.html` dengan menggunakan css dengan menggunakan kode ini:
```
  body {
      margin: 0;
      padding: 0;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      background-color: #ffffff; /* White background */
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      text-align: center;
      padding-top: 2%;
  }
  
  .logo {
  width: 300px; /* Adjust as needed */
  height: auto;
  margin-bottom: 10px;
  }
  
  .login {
  background-color: #f5f5dc; /* Beige box */
  padding: 60px 40px; 
  border-radius: 8px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.1);
  width: 500px;
  max-width: 80%; 
  }
  
  .form-control {
  width: 80%; 
  padding: 10px;
  margin: 10px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
  font-size: 16px; 
  text-align: start;
  }
  
  .login_btn {
  background-color: #4CAF50; /* Green */
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 80%; 
  font-size: 16px; 
  }
  
  .login_btn:hover {
  opacity: 0.8;
  }
  
  table {
  width: 100%;
  }
  
  td {
  padding: 8px;
  font-size: 16px; 
  }
  
  ul {
  list-style-type: none;
  padding: 0;
  }
  
  li {
  margin: 5px 0;
  color: red;
  font-size: 16px; 
  }
  
  a {
  color: #007bff;
  text-decoration: none;
  font-size: 16px; 
  }
  
  a:hover {
  text-decoration: underline;
  }
  
```

+ Kemudian customisasi halaman `register.html` dengan menggunakan css dengan menggunakan kode ini:
```
  body {
      margin: 0;
      padding: 0;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      background-color: #ffffff;
      display: flex;
      flex-direction: column;
      align-items: start;
      justify-content: flex-start;
      min-height: 100vh;
  }
  
  h1 {
      margin-bottom: 5%;
      padding-top: 2%;
      color: #333;
      font-weight: 300; 
      font-size: 32px; 
      letter-spacing: 7px;
  }
    
  .login {
      background-color: #f5f5dc; 
      padding: 2px 80px;
      border-radius: 8px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.1);
      width: 70%; /* Adjusted width */
      max-width: 90%;
      text-align: start;
  }
  
  .logo {
      width: 300px; 
      height: auto;
      margin-bottom: 10px;
  }
  
  table {
      width: 100%;
  }
  
  td {
      padding: 8px;
      font-size: 18px;
      vertical-align: middle;
  }
  
  input[type="submit"][name="submit"] {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
      font-size: 16px;
      border-radius: 4px;
      transition: background-color 0.3s;
      width: 90%; /* Adjusted width */
      margin-bottom: 4%;
  }
  
  input[type="submit"][name="submit"]:hover {
      opacity: 0.8;
  }
  
  ul {
      list-style-type: none;
      padding: 0;
      margin: 0; 
      width: 80%; 
      margin-left: auto; 
      margin-right: auto; 
      text-align: left; 
  }
    
  li {
      margin: 5px 0;
      color: #333;
      font-size: 16px;
  }

```
+ Kemudian customisasi tambah inventory yaitu halaman `create_product.html` dengan menggunakan css dengan menggunakan kode ini:
```
  body {
      margin: 0;
      padding: 0;
      font-family: 'Helvetica Neue', Arial, sans-serif;
      background-color: #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      padding-top: 5%;
  }
    
  h1 {
  margin-bottom: 20px;
  color: #333;
  font-weight: 300; 
  font-size: 32px; 
  }
  
  form {
  background-color: #f5f5dc; 
  padding: 20px 60px; 
  border-radius: 8px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.1);
  width: 600px; 
  max-width: 100%; 
  text-align: start;
  }
  
  table {
  width: 100%;
  margin: 25px 0; 
  }
  
  td {
  padding: 8px;
  font-size: 18px;
  vertical-align:auto;
  }
  
  input[type="submit"] {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
  width: 75%;
  margin-top: 20px;
  }
  
  input[type="submit"]:hover {
  background-color: #337736;
  }
  
  .back-button {
      padding: 10px 20px;
      background-color: #ccc;  
      color: #333;
      border: none;
      text-decoration: none;  
      display: inline-block;  
      border-radius: 4px;
      transition: background-color 0.3s;
      width: 75%;
      margin-top: 20px;
      text-align: center;
  }
  
  .back-button:hover {
      background-color: #bbb;  
  }
```

- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna<br>
+ Tambahkan Bootstrap untuk membuat tabel pada `main.html` dengan menambahkan kode ini:
```
 <div class="table-container"> 
        <h5>Kamu menyimpan {{total_item}} item pada aplikasi ini.</h5>   
        <table class="table table-bordered">
            <thead class="table-secondary">
```

+ Customisasi daftar inventory yaitu halaman `main.html` dengan menggunakan css dengan menggunakan kode ini:
```
  body {
      color: #333; /* dark text */
  }
  
  .tugas h1 {
      padding-top: 110px;
      font-family: Cambria;
      text-align: center;
      color: #333; /* dark text */
  }
  
  .tugas {
      background-color: rgb(222, 213, 206);
  }
  
  .profil {
      padding-top: 50px;
      padding-bottom: 10px;
      padding-left: 100px; 
      color: #333; /* dark text */
  }
  
  .table-container {
      padding-top: 50px;
      max-width: 1000px;
      margin: 0 auto;
  }
  
  .table {
      width: 100%;
      margin: 20px 0;
      border-collapse: collapse;
      background-color: #f9f9f9; 
  }
  
  .table th {
      padding: 10px;
      border: 1px solid #ccc;
      background-color: #f5f5dc; /* beige header */
  }
  
  .table td {
      padding: 10px;
      border: 1px solid #ccc;
  }
  
  .last-row {
      background-color: #ffe48a; 
  }
  
  button {
      padding: 8px 12px;
      cursor: pointer;
      background-color: #4CAF50; 
      color: white;
      border: none;
      border-radius: 4px;
      transition: background-color 0.3s;
  }
  
  button:hover {
      background-color: #45a049; 
  }
  
  h4{
      padding-bottom: 5%;
  }
  
  a{
      padding-top: 5%;
      text-decoration: none;
  }
  
  .btn {
      display: inline-block;
      padding: 10px 20px;
      font-size: 16px;
      color: #fff;
      background-color: #4CAF50;
      border: none;
      text-decoration: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s;
      align-items: center;
      width: 200px;
  }
  
  .btn:hover {
      background-color: #45a049;  
  }
  
  .button-container {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px; 
  }
```

## **Melakukan add-commit-push ke GitHub**



# **Tugas 4 - Pemrograman Berbasis Platform**

**I Made Surya Anahata Putra**<br/>
**2206081370**<br/>
**PBP A**<br/>

## **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
`UserCreationForm` dalam Django adalah sebuah formulir bawaan yang disediakan oleh kerangka kerja Django untuk memudahkan proses pendaftaran pengguna dalam aplikasi web. Form ini telah dirancang khusus untuk mencakup bidang seperti nama pengguna, kata sandi, dan konfirmasi kata sandi. Kelebihan utamanya adalah kemudahannya dalam penggunaan dan integrasinya yang lancar dengan model pengguna bawaan Django. Form ini juga mencakup validasi otomatis untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan persyaratan yang ditetapkan. Selain itu, penggunaan `UserCreationForm` dapat menghemat waktu pengembangan karena pengembang tidak perlu membuat formulir pendaftaran dari awal. Namun, perlu diperhatikan bahwa dalam beberapa situasi, perlu adanya tampilan atau logika tambahan sesuai dengan kebutuhan khusus aplikasi, karena form ini mungkin memiliki keterbatasan dalam hal kustomisasi dan tampilan yang sangat spesifik.<br>

Kelebihan utama dari `UserCreationForm` adalah:
+ Kemudahan Penggunaan<br> 
Form ini sudah tersedia dan siap digunakan dengan konfigurasi standar. Kita dapat menggunakannya dengan mudah tanpa perlu membuat formulir pendaftaran dari awal.
+ Validasi Terintegrasi<br>
Form ini memiliki validasi bawaan yang membantu memastikan kebenaran data yang dimasukkan oleh pengguna, seperti memastikan kata sandi cocok dengan konfirmasi kata sandi.
+ Integrasi Model User<br>
Form ini bekerja dengan model pengguna bawaan Django (User) dengan baik, sehingga ketika data dimasukkan dan disubmit, akun pengguna baru akan dibuat dan disimpan di database secara otomatis.<br>

Kekurangan dari UserCreationForm:

+ Kustomisasi Terbatas<br>
Meskipun UserCreationForm menyediakan fungsi dasar untuk pendaftaran pengguna, dalam banyak kasus kita akan perlu menyesuaikan tampilan dan perilaku form untuk memenuhi kebutuhan aplikasi kita. Ini bisa memerlukan pembuatan form pendaftaran yang lebih kompleks atau penanganan kasus khusus yang tidak dicakup oleh UserCreationForm.
+ Tampilan Terbatas<br>
Form ini hanya menyediakan elemen dasar seperti teks input untuk username dan password. Jika kita memerlukan form pendaftaran yang lebih kaya dalam hal tampilan seperti pengecekan kekuatan kata sandi atau bidang tambahan seperti nama lengkap atau foto profil, kita masih perlu menambahkan kode tambahan.
+ Dibutuhkan Integrasi dengan Tampilan dan Logika Tambahan<br>
Untuk mengimplementasikan pendaftaran pengguna sepenuhnya, kita perlu mengintegrasikan UserCreationForm dengan tampilan (views) dan logika tambahan seperti penanganan pesan kesalahan, pengiriman email konfirmasi, dan verifikasi CAPTCHA jika diperlukan.

## **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
Dalam konteks Django, autentikasi dan otorisasi adalah dua konsep kunci yang berkaitan dengan keamanan pengguna dan akses pada aplikasi web. Perbedaan keduanya yaitu:

Autentikasi:
+ Autentikasi adalah proses verifikasi identitas pengguna. Ini menentukan apakah seorang pengguna adalah orang yang mereka klaim sebagai, yaitu apakah mereka memiliki akun atau kredensial yang valid untuk mengakses sistem.<br>
+ Dalam Django, autentikasi umumnya melibatkan proses verifikasi identitas pengguna melalui penggunaan nama pengguna (username) dan kata sandi (password) yang valid. Django memiliki sistem otentikasi yang kuat yang memungkinkan pengguna mendaftar, masuk (login), dan keluar (logout) dari aplikasi.<br>
+ Autentikasi digunakan untuk memastikan bahwa hanya pengguna yang sah yang memiliki akses ke sumber daya dan fitur tertentu di dalam aplikasi. Ini membantu melindungi informasi sensitif dan menjaga keamanan akun pengguna.<br>

Otorisasi:
+ Otorisasi adalah proses yang menentukan apa yang diizinkan atau dilarang oleh pengguna yang sudah diautentikasi. Ini adalah tentang mengendalikan akses ke sumber daya atau fitur tertentu berdasarkan hak akses pengguna.<br>
+ Dalam Django, otorisasi biasanya diatur dengan menggunakan dekorator atau middleware yang memeriksa izin (permissions) pengguna. Django memiliki sistem otorisasi yang memungkinkan kita untuk menentukan siapa yang memiliki akses ke halaman web tertentu, apa yang dapat mereka lakukan (misalnya, hanya pengguna tertentu yang dapat mengedit atau menghapus data), dan sebagainya.<br>
+ Otorisasi penting untuk memastikan bahwa setiap pengguna hanya dapat mengakses sumber daya atau melakukan tindakan yang sesuai dengan peran atau izin mereka. Ini membantu menjaga integritas data dan mengendalikan tingkat akses yang sesuai dalam aplikasi.<br>
  
Keduanya penting karena mereka saling melengkapi dalam menciptakan aplikasi web yang aman dan fungsional. Autentikasi memastikan bahwa pengguna yang masuk adalah pengguna yang sah, sedangkan otorisasi memastikan bahwa pengguna yang diautentikasi hanya memiliki akses ke bagian aplikasi yang sesuai dengan peran atau izin mereka.

## **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
Dalam konteks aplikasi web, cookies adalah mekanisme kecil untuk menyimpan data pada sisi klien (browser) dengan tujuan untuk mengidentifikasi atau melacak informasi tertentu terkait dengan sesi pengguna atau interaksi pengguna dengan situs web. Cookies sering digunakan untuk menyimpan informasi seperti preferensi pengguna, data masuk (login), keranjang belanja, dan banyak lagi.<br>

Django menggunakan cookies sebagai salah satu cara untuk mengelola data sesi pengguna. Sesi pengguna adalah cara untuk menyimpan informasi yang berkaitan dengan pengguna tertentu selama sesi mereka di dalam situs web. Contoh penggunaan cookies dalam Django untuk mengelola data sesi pengguna adalah sebagai berikut:

+ Mengidentifikasi Sesi Pengguna<br>Ketika seorang pengguna pertama kali mengunjungi situs web kita, Django dapat menghasilkan cookie unik untuk mengidentifikasi sesi pengguna tersebut. Ini memungkinkan server untuk mengenali pengguna yang sama yang kembali ke situs web dalam kunjungan berikutnya.

+ Penyimpanan Data Sesi<br>Django dapat menggunakan cookies untuk menyimpan data sesi pengguna seperti informasi masuk, preferensi, atau item dalam keranjang belanja. Data ini dapat dienkripsi atau diubah sedemikian rupa sehingga hanya server yang dapat membacanya.

+ Manajemen Otentikasi<br>Cookies juga dapat digunakan untuk mengelola proses otentikasi pengguna. Misalnya, ketika seorang pengguna masuk ke situs web, server dapat menghasilkan cookie otentikasi yang memberikan akses ke halaman yang dilindungi tanpa perlu login ulang setiap saat.

Django menyediakan dukungan bawaan untuk mengelola data sesi pengguna dengan menggunakan cookies melalui modul django.contrib.sessions.middleware.SessionMiddleware dan konfigurasi di dalam file settings.py. Kita dapat mengatur jenis penyimpanan sesi yang berbeda seperti penyimpanan berbasis database, penyimpanan berbasis cache, atau penyimpanan berbasis file sesuai dengan kebutuhan.

## **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
Penggunaan cookies sendiri tidak memiliki masalah keamanan secara inheren, tetapi bagaimana mereka digunakan dan disimpan oleh aplikasi web dapat menjadi sumber masalah. Cookies dalam pengembangan web memiliki potensi risiko yang perlu diwaspadai. Berikut adalah beberapa risiko potensial yang terkait dengan penggunaan cookies:

+ Pencurian Data: Jika cookies mengandung informasi sensitif seperti token otentikasi atau data pribadi pengguna, cookies ini dapat menjadi target potensial bagi penyerang yang ingin mencuri data tersebut.

+ Cross-Site Scripting (XSS): Jika aplikasi web rentan terhadap serangan XSS, penyerang dapat mencuri cookies pengguna dan mendapatkan akses ke data yang tersimpan dalam cookies. Oleh karena itu, menjaga keamanan aplikasi web sangat penting.

+ Session Hijacking: Jika cookies digunakan untuk menyimpan ID sesi (session ID) pengguna, penyerang yang berhasil mencuri cookies ini dapat mengambil alih sesi pengguna tanpa perlu login ulang.

+ Man-in-the-Middle Attacks: Penyerang dapat mencuri cookies saat data dikirimkan antara browser pengguna dan server jika koneksi tidak aman. Menggunakan HTTPS adalah cara umum untuk mengurangi risiko ini.

+ Penggunaan Cookies oleh Pihak Ketiga: Cookies sering digunakan oleh perusahaan periklanan dan analitik untuk melacak perilaku pengguna di seluruh web. Hal ini dapat mengancam privasi pengguna dan menghasilkan risiko terkait privasi.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar<br>

_REGISTRASI_
+ Jalankan virtual environment terlebih dahulu.
+ Buka views.py yang ada pada direktori root dan buatlah fungsi dengan nama register yang menerima parameter request.
+ Tambahkan import redirect, UserCreationForm, dan messages pada bagian paling atas.
  ```
  from django.shortcuts import redirect
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib import messages  
  ```
+ Tambahkan potongan kode di bawah ini ke dalam fungsi register yang sudah dibuat sebelumnya.
  ```
  def register(request):
      form = UserCreationForm()
  
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('login')
      context = {'form':form}
      return render(request, 'register.html', context)
  ```
+ Buatlah berkas HTML baru dengan nama register.html pada folder root templates. Isi dari register.html dapat diisi dengan template berikut:
  ```
      {% extends 'base.html' %}
      
      {% block meta %}
          <title>Register</title>
      {% endblock meta %}
      
      {% block content %}  
      
      <div class = "login">
          
          <h1>Register</h1>  
      
              <form method="POST" >  
                  {% csrf_token %}  
                  <table>  
                      {{ form.as_table }}  
                      <tr>  
                          <td></td>
                          <td><input type="submit" name="submit" value="Daftar"/></td>  
                      </tr>  
                  </table>  
              </form>
      
          {% if messages %}  
              <ul>   
                  {% for message in messages %}  
                      <li>{{ message }}</li>  
                      {% endfor %}  
              </ul>   
          {% endif %}
      
      </div>  
      
      {% endblock content %}
  ```
+ Buka urls.py yang ada pada subdirektori root dan impor fungsi yang sudah dibuat tadi.
  ```
    from main.views import register
  ```
  
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
  ```
    ...
      path('register/', register, name='register'),
    ...
  ```

_LOGIN_
+ Jalankan virtual environment terlebih dahulu.
+ Buka views.py yang ada pada direktori root dan buatlah fungsi dengan nama login_user yang menerima parameter request.
+ Tambahkan import authenticate dan login pada bagian paling atas.
  ```
    from django.contrib.auth import authenticate, login 
  ```
+ Tambahkan potongan kode di bawah ini ke dalam fungsi login yang sudah dibuat sebelumnya. Potongan kode ini berfungsi untuk mengautentikasi pengguna yang ingin login.
  ```
  def login_user(request):
      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              response = HttpResponseRedirect(reverse("main:show_main")) 
              response.set_cookie('last_login', str(datetime.datetime.now()))
              return response
          else:
              messages.info(request, 'Sorry, incorrect username or password. Please try again.')
      context = {}
      return render(request, 'login.html', context)
  ```
+ Buatlah berkas HTML baru dengan nama login.html pada folder root templates. Isi dari login.html dapat diisi dengan template berikut.
  ```
    {% extends 'base.html' %}
    
    {% block meta %}
        <title>Login</title>
    {% endblock meta %}
    
    {% block content %}
    
    <div class = "login">
    
        <h1>Login</h1>
    
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>
    
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>
    
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
    
    </div>
    
    {% endblock content %}
  ```
+ Buka urls.py yang ada pada subdirektori root dan impor fungsi yang sudah dibuat tadi.
  ```
    from main.views import login_user
  ```
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
  ```
    ...
      path('login/', login_user, name='login'),
    ...
  ```
_LOGOUT_
+ Buka views.py yang ada pada subdirektori main dan buatlah fungsi dengan nama logout_user yang menerima parameter request
+ Tambahkan import logout pada bagian paling atas.
```from django.contrib.auth import logout```
+ Tambahkan potongan kode di bawah ini ke dalam fungsi logout yang sudah dibuat sebelumnya. Potongan kode ini berfungsi untuk melakukan mekanisme logout:
  ```
  def logout_user(request):
      logout(request)
      return redirect('main:login')
  ```
+ Bukalah berkas main.html yang ada pada folder main/templates dan tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Product pada berkas main.html
  ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
  ```
+ Buka urls.py yang ada pada subdirektori main dan impor fungsi yang sudah dibuat tadi.
  ```
  from main.views import logout_user
  ```
+ Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
```
  ...
  path('logout/', logout_user, name='logout'),
  ...
```
+ Selanjutnya tambahkan restriksi pada halaman main agar sesuai dengan user yang sedang login. Pertama-tama buka berkas `views.py` yang ada pada direktori `main` dan tambahkan import `login_required` pada bagian atas
```
  from django.contrib.auth.decorators import login_required
```
+ Tambahkan juga kode `@login_required(login_url='/login')` di atas fungsi `show_main`.
```
  ...
  @login_required(login_url='/login')
  def show_main(request):
  ...
```

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal<br>
+ Pertama buka http://127.0.0.1:8000/ pada browser.
+ Lalu tekan tombol main kemudian tekan tombol `Register Now` untuk membuat 2 akun baru
+ Setelah selesai membuat 2 akun baru lalu, login dengan username dan password sesuai dengan yang sudah dibuat pada form register
+ Lalu tekan tombol `add new product` untuk membuat dummy data, dan buatlah masing-masing 3 dummy data per akun.
+ Dua akun pengguna dengan masing-masing 3 dummy data berhasil dibuat!
  
- [x] Menghubungkan model Item dengan User<br>
  + Buka berkas `models.py` pada direktori `main` dan tambahkan kode berikut.
  ```
    ...
    from django.contrib.auth.models import User
    ...
  ```
+ Tambahkan juga pada model `Item` yang sudah dibuat potongan kode berikut.
```
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
+ Buka `views.py` pada direktori `main` dan ubah potongan kode pada `create_product` menjadi seperti dibawah ini.
```
  def create_product(request):
   form = ProductForm(request.POST or None)
  
   if form.is_valid() and request.method == "POST":
       product = form.save(commit=False)
       product.user = request.user
       product.save()
       return HttpResponseRedirect(reverse('main:show_main'))
   ...
```
+ Pada fungsi `show_main` juga ubah menjadi seperti berikut.
```
  def show_main(request):
      products = Product.objects.filter(user=request.user)
  
      context = {
          ...
          'name': request.user.username,
      ...
      }
```
+ Simpan semua perubahan dengan melakukan `python manage.py makemigrations`.
+ Seharusnya akan muncul error saat melakukan migrasi model. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data.
+ Ketik angka 1 kembali untuk menetapkan dengan user ID 1
+ Lakukan `python manage.py migrate` kembali untuk mengaplikasikan yang dilakukan pada sebelumnya
<br>

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi<br>

+ Untuk menampilkan username nama yang sedang logged in sudah terdapat pada step sebelumnya yaitu saat tahap mengganti context di dalam `show_main` yaitu  
```
'name': request.user.username,
```
+ Untuk menerapkan cookies seperti last login, pertama-tama kita harus menghubungan data dari cookies terlebih dahulu. Buka berkas `views.py` pada direktori `main` dan tambahkan beberapa import dibawah ini.
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
+ Pada fungsi `login_user`, tambahkan fungsi untuk menambahkan cookie yang bernama `last_login` untuk melihat kapan kali suatu user melakukan login. Caranya adalah dengan mengganti kode yang ada pada blok `if user is not None` menjadi potongan kode dibawah ini.
```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
+ Pada fungsi `show_main` tambahkan potongan kode `last_login': request.COOKIES['last_login']` ke dalam variable context.
```
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    ...
}
```
+ Ubah fungsi `logout_user` menjadi potongan berikut.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
+ Buka berkas `main.html` dan tambahkan potongan kode berikut di bawah tombol logout.
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
+ Refresh halaman login (atau jalankan proyek Django dengan perintah python manage.py runserver) dan cobalah untuk login. Data last login akan muncul di halaman main.
  
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



