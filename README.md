﻿
# Pemograman Berbasis Platform C
## MamPedia
### Sebuah proyek Django sederhana Tugas Mata Kuliah Pemrograman Berbasis Platform oleh **Imam Fajri 2306165566**.
### Link PWS : http://imam-fajri-mampedia.pbp.cs.ui.ac.id/ (Status:Offline)
---
# Penjelasan Tutorial dan menjawab semua jawaban

<details>
<summary>Click for more detail</summary>
<br>

# Tugas 2 Implementasi Model-View-Template (MVT) pada Django

<details>
<summary>Click for more detail</summary>
<br>

### Proses Pembuatan Projek Django
1. Membuat sebuah _repository_ Github baru bernama ```mampedia```
2. Meng-_clone repostiory_ kosong tersebut ke komputer
3. Di direktori asal Membuat _virtual environment_ Python baru dengan command:

    ```bash
    python -m venv env
    ```
4. Menyalakan _virtual environment_ Python baru dengan command:
    ```bash
    source env/bin/activate
    ```
5. Mempersiapkan _requirements_ dengan _neovim_
    ```bash
    nvim requirements.txt
    ```
    isi dari requirements.txt
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
6. Meng-_install requirements_ dengan pip
    ```bash
    Python -m pip install -r requirements.txt
    ```
7. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject mampedia .
    ```
8. Mengubah ```ALLOWED_HOSTS``` di file ```settings.py``` dengan menambahkan ```"*"``` agar proyek ini bisa dijalankan di host/domain apapun.

9. Membuat aplikasi ```main``` dengan command:
    ```bash
    python manage.py startapp main
    ```
10. Menambahkan nama aplikasi ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```mampedia```

11. Me-_routing_ url pada file ```urls.py``` di direktori ```mampedia``` sehingga isi file ```urls.py``` menjadi:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
12. Mengubah ```models.py``` menjadi:
    ```python
    from django.db import models

    class Atribut(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField
        description = models.TextField
        quantity = models.IntegerField
    ```
13. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
14. Membuat direktori template dan template ```html``` untuk laman ```main```:

    ```html
    <h1>MamPedia Semua Ada</h1>
    <h4>NPM: 2306165566</h4>
    <h4>Name: Imam Fajri</h5>
    <h4>Class: PBP C</h4>
    <h5>Nama Pesanan</h5>
    <p>{{ name }}<p>
    <h6>Harga</h6>
    <p>{{ price }}<p>
    <h5>Jumlah Pesanan</h5>
    <p>{{ quantity }}<p>
    <h6>Deksripsi</h6>
    <p>{{ description }}<p>
    ```
15. Menambahkan fungsi untuk me-_render_ laman main pada file ```views.py```:
    ```python
    from django.shortcuts import render

    def show_main(request):
    context = {
        'name' : 'Sate Pacil',
        'price': 'Rp.15.000',
        'quantity': '1',
        'description': 'Sate adalah makanan ayam yang sangat enak',
    }

        return render(request, "main.html", context)
    ```

16. Melakukan routing pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

17. Mengetest aplikasi pada localhost dengan command:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_

18. Melakukan deploy app ke situs _PWS (Pacil Web Service)_

**Bagan Arsitektur Django**
![](static/MVT.png)
Terlihat bahwa _request_  dari user akan diproses terlebih dahulu sehingga dapat diteruskan ke View yang sesuai. kemudian View tersebut akan membaca/menulis data di Model dan menggunakan Template yang berisi file HTML untuk menampilkan dan mengembalikan _response_ ke _user_

**Fungsi git dalam pengembangan perangkat lunak**

Git adalah alat pengembangan perangkat lunak yang berfungsi sebagai sistem kontrol untuk menyimpan, mengelola, dan berbagi kode dengan developer lain secara efisien.Git juga dapat melacak seluruh history perubahan yang dilakukan pada kode sumber sehingga memungkinkan seluruh kode yang dibuat oleh tim dapat dikontrol dan diperbaiki jika ada kesalahan. Selain itu git dapat menangani proyek dari ukuran kecil hingga sangat besar dengan jutaan baris kode dan ribuan pengembang.

**Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak**

Karena pada saat semester 1 bahasa pemograman pertama yang diajarkan adalah python yang sangat mudah dipahami, disatu sisi framework ini menyediakan banyak fitur seperti:

+ ORM, atau object relational model yang memberikan pengembang cara mudah untuk melaksanakan CRUD(Create, Retrive, Update, Delete) pada database setelah model dibuat.
+ Database Migration, saat struktur database perlu diubah, django membuatnya sangat mudah bagi pengembang.
+ MVT, dengan MVT, django menggunakan sistem antarmuka yang intuitif dan mengedepankan pengembangan terstruktur.
+ Powerfull Routing, Django menyediakan alat routing yang mudah, dengan dynamic URLS.
+ Essentials built-in, fitur seperti admin, autentikasi, users sudah ada di Django sehingga pengembang dapat fokus ke logic utama aplikasinya.

Selain itu, dukungan dari komunitas yang berguna untuk membantu jika ada masalah terkait pengembangan web.

**Mengapa model pada Django disebut sebagai ORM**

Karena Django menggunakan pemetaan objek-relasional (ORM) untuk menyederhanakan interaksi dengan basis data tanpa perlu melakukan kueri SQL yang rumit. Dalam Django, model adalah representasi dari tabel dalam database, dan setiap field dalam model merepresentasikan kolom dalam tabel. ORM ini membantu mengelola dan memanipulasi data dalam database dengan menggunakan method di Python tanpa perlu menulis SQL secara manual.
fitur yang ada pada ORM meliputi
+ Mapping antara Objek dan Database, Kelas model Django dihubungkan ke tabel database, di mana setiap instance dari model merepresentasikan satu baris data di database.
+ Abstraksi Database, ORM memungkinkan untuk menggunakan berbagai database (MySQL, PostgreSQL, SQLite, dll.) tanpa perlu mengubah kode Python, cukup mengubah konfigurasi database.
+ CRUD Operations, Django ORM menyediakan cara mudah untuk melakukan operasi CRUD (Create, Read, Update, Delete) dengan cara Pythonik seperti Model.objects.create(), Model.objects.filter(), dan Model.objects.delete().Berikut ini contoh`:

```python
from django.db import models

class Atribut(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

```
</details>

# Tugas 3 Implementasi Form dan Data Delivery pada Django
<details>
<summary>Click for more detail</summary>
<br>

## Pentingnya Data Delivery dalam Mengimplementasikan sebuah Platform

Pentingnya data delivery dalam pengembangan platform adalah pengguna dan developer mendapatkan dan mengirim data yang mereka butuhkan dengan cepat dan efisien sehingga dapat mempercepat proses loading data pada platform yang digunakan. Data delivery dapat melakukan pertukaran data antar komponen platform yang berbeda tergantung dengan format yang dibutuhkan seperti `JSON`, `XML`, dan `HTML`. Selain itu melalui data delivery, developers juga dapat mengirimkan data ke berbagai lokasi seperti server, cloud, dan Contrn Delivery Network (CDN). Dengan begitu aplikasi web yang dibuat lebih scalable dan dapat diakses dari berbagi lokasi.

## Perbedaan XML dan JSON
**Pendapat Saya XML dan JSON yang lebih baik**

Mana yang lebih baik antara XML dan JSON, Karena saya hanya mengembangkan website yang tidak memerlukan data yang kompleks dan validasi data yang mendalam saya memilih **JSON**. Alasannya adalah formatnya yang ringan, deskriptif, mudah dibaca, dan kompetibel dengan kerangka kerja JavaScript, serta mendukung penguraian yang cepat. 

**Alasan JSON lebih populer**

karena format yang lebih sederhana dan ringkas, JSON menawarkan kinerja yang lebih baik dan komunikasi yang lebih cepat.

## Fungsi Method `is_valid()` pada django dan kebutuhan method tersebut

Fungsi dari method `is_valid()` pada form Django adalah untuk memvalidasi data yang dimasukkan oleh user sebelum disimpan ke database. Method `is_valid()` akan mengembalikan nilai `True` atau `False` tergantung tipe yang diizinkan.
Dengan menggunakan method `is_valid()`, developers dapat memastikan bahwa data yang dimasukkan oleh user valid dan sesuai dengan aturan yang telah ditentukan. Method `is_valid()` juga memungkinkan developers untuk menampilkan pesan error jika data yang dimasukkan oleh user tidak valid. Dengan menggunakan method `is_valid()`,
Contoh penggunaan method `is_valid()`:
```python
if form.is_valid():
    form.save()
else:
    print(form.errors)
```

Contoh input yang tidak valid:
```python
form = AtributEntryForm(data={'name': '1234567891011...256', 'price': 100, 'description': 'tes', 'stock': 100})
```
`'name'` harus kurang dari 255 karakter. Anggap string tersebut memiliki 256 karakter.

Contoh output:
```python
{'name': ['Ensure this value has at most 255 characters (it has 256).']}
```
## Alasan membutuhkan `crf_token` dalam membuat form
karena `csrf_token` berfungsi untuk security yang dibuat secara otomatis oleh Django untuk mencegah serangan berbahaya terhadap aplikasi web kita.

**Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?**
Apabila tidak menggunakan `csrf_token` Django akan menolak request POST, karena django akan memblokir request tersebut karena dianggap tidak aman kemudian akan mendapatkan kesalahan `403 Forbidden` yang berarti server menolak untuk memproses request.

**Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
Penyerang bisa membuat sebuah situs palsu atau mengirimkan email yang mengandung `form` tersembunyi yang melakukan aksi ke server kita. Jika pengguna mengklik tautan atau membuka halaman tersebut dan mereka sudah login ke situs kita, browser mereka akan mengirimkan request tanpa disadari pengguna, membuat serangan itu berhasil.Menggunakan `csrf_token` memastikan bahwa request hanya valid jika berasal dari `form` yang dibuat oleh server, karena token tersebut unik untuk setiap sesi dan request, sehingga serangan ini dapat dicegah.

## Proses mengimplementasi Form dan Data Delivery

#### Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Membuat folder templates yang berisi base.html pada root folder dan menambahkannya pada `settings.py`. `base.html` ini akan menjadi template html project ini untuk kedepannya.
- Melengkapi kerangka yang terdapat pada `base.html` untuk kebutuhan aplikasi main berupa atribut form untuk menerima input user dan mendisplay hasil dari input tersebut.
- Membuat file baru bernama `forms.py`. File ini akan berperan sebagai struktur form yang dapat menerima input data oleh user.
- Membuat `create_atribute_entry.html` di folder `templates/main dengan tujuan membuat form untuk menambahkan produk
- Menambahkan `csrf_token` pada form di `create_atribute_entry.html` untuk mencegah serangan CSRF.

#### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Fungsi dalam format XML dan JSON menambahkan variable yang menyimpan objects pada item dan mereturn HttpResponse  yang isi parameternya adalah objects yang diserialisasi.
- Fungsi XML by ID dan JSON by ID sama implementasinya dengan XML dan JSON biasa namun untuk variable yang menyimpan objects menggunakan filter `(pk=id)` sehingga dapat diurutkan berdasarkan input. Berikut adalah kodenya
``` python
def show_xml(request):
    data = AtributEntery.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AtributEntery.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AtributEntery.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Pada urls.py, tambahkan beberapa import terhadap setiap fungsi yang terdapat pada views.
  ``` python
  from main.views import show_main, create_atribute_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
  ```
- Untuk fungsi create_cat_entry, XML, dan JSON tambahkan path yang sesuai.
```python
  path('create-atribute-entry', create_atribute_entry, name='create_atribute_entry'),
  path('xml/', show_xml, name='show_xml'),
  path('json/', show_json, name='show_json'),
```
- Untuk fungsi XML by ID dan JSON by ID path ditambahkan `<str:id>` untuk mendapatkan data sesuai dengan id
```python
  path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
  path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

## Penggunaan Postman
#### XML

![](static/dataXML.png)

#### JSON

![](static/dataJSON.png)

#### XML by ID

![](static/dataXMLID.png)

#### JSON by ID

![](static/dataJSONID.png)

</details>

# Tugas 4 Implementasi Autentikasi, Session, dan Cookies pada Django
<details>
<summary>Click for more detail</summary>
<br>

## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

`HttpResponseRedirect()` dan `redirect()` pada dasarnya memiliki kesamaan fungsi yang sama yaitu untuk mengarahkan pengguna ke URL lain. Namun, terdapat perbedaan yaitu `HttpResponseRedirect()` adalah kelas Django yang secara eksplisit membuat respons HTTP dengan kode status 302 `(redirect)` dan URL tujuan. Sementara itu, `redirect()` adalah fungsi bawaan Django yang mempermudah proses pengalihan `(redirect)` dengan menerima argumen seperti URL, view name, atau objek model dan secara otomatis menghasilkan `HttpResponseRedirect()` di balik layar. Jadi, perbedan utama terletak dimana `HttpResponseRedirect()` mengharuskan URL penuh sebagai argumen, sedangkan `redirect()` lebih fleksibel dan menangani detail pembuatan respons redirect.

## Cara kerja penghubungan model Product dengan User

Untuk menghubungkan model `Product` dengan model `User` dalam Django, kita bisa menggunakan `ForeignKey` atau `ManyToManyField`, tergantung pada jenis relasi yang diinginkan. Dalam hal ini projek saya menggunakan `ForeignKey`. Pada model `AtributEntery` setiap entry atribut dihubungkan dengan pengguna melalui `ForeignKey` pada field user. Field id menggunakan `UUIDField` sebagai primary key yang dihasilkan secara otomatis menggunakan library bawaan `uuid.uuid4`. Ini memberikan identifikasi unik dan membuat aplikasi menjadi lebih aman untuk setiap catatan. `ForeignKey` itu sendiri digunakan untuk jika setiap produk dimiliki oleh satu pengguna.

## Perbedaan antara autentikasi dan otorisasi dalam konteks Django dan bagaimana Django mengimplementasikan kedua konsep tersebut.

- Autentikasi : Proses untuk melakukan **verifikasi pengguna** untuk melakukan login. Dalam konteks django, django telah menyediakan sistem autentikasi bawaan yang mencakup user accounts, groups, permissions dan cookie-based user sessions.
- Otorisasi : Proses **menentukan hak akses pengguna** setelah pengguna terautentikasi. 
- Implementasi authentication di Django menggunakan model User yang disediakan oleh modul `django.contrib.auth` untuk menangani autentikasi.Fungsi `authenticate()` memverifikasi kredensial pengguna, dan jika valid, mengembalikan objek User.Setelah terautentikasi, Django menggunakan fungsi `login()` untuk mencatat bahwa pengguna tersebut telah berhasil login dan mengelola sesi pengguna. Untuk authorization Django mengimplementasikannya menggunakan permissions dan groups. Permissions adalah aturan yang menetapkan apa yang dapat dilakukan pengguna (misalnya, "add", "change", "delete", atau hak akses custom). Django secara otomatis menambahkan permissions untuk setiap model (`add`, `change`, `delete`), tetapi kita juga bisa membuat permissions kustom. Otorisasi diperiksa menggunakan decorator atau middleware. Django juga mendukung groups, yang memungkinkan kita mengelompokkan pengguna dan memberikan izin secara kolektif berdasarkan grup.

## Cara django untuk mengingat pengguna yang telah login dan kegunaan lain dari cookies dan apakah semua cookies aman digunakan

Django mengingat pengguna yang telah login menggunakan `session`. Saat pengguna login, Django membuat session dan menyimpan informasi pengguna seperti ID atau status login di server. Sebuah cookie dengan ID session dikirim ke browser pengguna. Setiap kali pengguna mengirim permintaan ke server, cookie ini dikirim kembali ke server, memungkinkan Django untuk mengidentifikasi pengguna yang telah login. Dengan cara ini, Django dapat mengingat pengguna antara pemintaan, meskipun HTTP adaah protokol tanpa status atau not secure.

Selain itu cookie digunakan untuk menyimpan preferensi pengguna, mengetahui aktifitas, dan mengidentifikasi pengguna yang telah mengunjungi situs web sebelumnya. Cookies secara default cukup aman dan tidak dapat menyebar virus atau malvare, namun dapat menimbulkan beberapa masalah privasi dan keamanan jika tidak ditangani dengan benar. Beberapa potensi resiko yang harus diwaspadai, yaitu:
- Melacak aktivitas pengguna dan menyimpan data pengguna tanpa izin.
- Session fixation dan session hijacking yang mana memaksa pengguna untuk menggunakan session id penyerang,
- Menerima cookies dari situs palsu atau sumber yang tidak kredibel: dapat terkena tindakan phising.
- Memiliki cookies dengan waktu kadaluwarsa yang panjang: berbahaya sebab dapat diretas oleh pihak ketiga.

Jadi cookies sebenarnya aman dipakai tetapi harus diatur dengan menggunakan `session id` yang unik sebagai data yang dikirim pada cookies agar lebih aman.

## Proses Implementasi Autentikasi, Session, dan Cookies pada tugas 4

#### Membuat Fungsi register, login_user, dan logout_user di dalam `models.py` pada direktori `main` 

```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
```
#### Membuat berkas `register.html` dan `login.html` untuk tampilan login dan registernya. Serta menambahkan tampilan tombol logout dan `{{ last_login }}` di berkas `main.html`.

- `register.html`
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
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

- `login.html`
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
- tambahan di `main.html`
```html
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    <a href="{% url 'main:logout' %}">
  <button>Logout</button>
    </a>
```

#### Merestriksi akses halaman Main agar login terlebih dahulu

Menambahkan kode @login_required(login_url='/login') di atas fungsi show_main.
```python
@login_required(login_url='/login')
    def show_main(request):
        atribut_entries = AtributEntery.objects.filter(user=request.user)
        context = {
            'npm' : '2306165566',
            'name': request.user.username,
            'class': 'PBP C',
            'atribut_entries': atribut_entries,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)
```

#### Jalankan server dengan perintah `runserver` kemudian membuat 2 akun baru dan menambahkan tigas dummy data

- username1: ImamGanteng; pass: imam12345
- username2: ImamKece; pass: imam12345

#### Menghubungkan model Product dengan User

- Mengimport modul `User` dari `django.contrib.auth.models`, lalu menambahkan model `user` ke class `AtributEntery` dengan menggunakan code `user = models.ForeignKey(User, on_delete=models.CASCADE)`
```python
    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
    class AtributEntery(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        time = models.DateField(auto_now_add=True)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField()
```

- Mengedit fungsi `create_atribute_entry` agar Django tidak langsung menyimpan objek yg di buat ke database.
```python
    def create_atribute_entry(request):
        form = AtributEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            atribute_entry = form.save(commit=False)
            atribute_entry.user =request.user
            atribute_entry.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_atribute_entry.html", context)
```

- Mengubah fungsi show_main pada bagian `name` agar yang muncul merupakan username yang sedang login.
` 'name': request.user.username,`

- Melakukan makemigration dan migrate.

#### Mengimpor date time. Lalu di login_user membuat fungsi baru yang dapat menambahkan cookie.

- Menambahkan last_login pada show_main di dalam `views.py` pada direktori `main`
`last_login': request.COOKIES['last_login'],`

- Mengubah logout_user untuk menghapus cookie setiap kali logout di dalam `views.py` pada direktori `main`
`response.delete_cookie('last_login')`
` 