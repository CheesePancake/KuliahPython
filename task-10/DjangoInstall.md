# Modul django task 10 pdf 1 ~ 4 kelas Pemrograman Python
Untuk task ini direkomendasikan untuk melakukan instalasi dan penerapan virtualenv atau virtual environment agar modul-modul paket python global tidak bentrok

Catatan : **Seluruh Perintah / Command dibawah diketik menggunakan terminal bash**

## ⚒️ Instalasi Django
- Aktifkan virtualenv yang sudah dibuat [sebelumnya](https://github.com/CheesePancake/KuliahPython/blob/main/task-10/readme.md) dengan perintah berikut :
```bash
$ source env/Scripts/activate
```
- Untuk tugas ini saya menginstall django framework versi 4.2.1 dengan perintah berikut :
```bash
$ pip install Django==4.2.1
```
## ⚙️ Memulai project django
- Saya akan membuat sebuah project django dengan nama **websiteku** dengan perintah berikut
```bash
$ django-admin startproject websiteku
```
- Munculnya folder **websiteku** dibawah folder **env** menandakan project telah dibuat
pindah dari folder **task-10** ke folder **websiteku** dengan perintah berikut :
```bash
$ cd websiteku
```
- Jalankan project django dengan perintah berikut :
```bash 
$ py manage.py runserver
```
ketika berhasil menjalankan perintah diatas, log terminal akan menampilkan link localhost untuk mengakses **websiteku** seperti ini
```
$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 11, 2023 - 22:49:18
Django version 4.2.1, using settings 'websiteku.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## 🖼️ Tampilan
 - tampilan awal **websiteku** di pc saya seperti ini 
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/1014a0ee-3c91-4311-96fc-eb3e0c6f2653">

- Struktur file django yang berhasil dijalankan
<img width="163" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/b1a23540-0c5b-480b-bbc1-ebb55f0d50c1">

# Selanjutnya
- 💼 [templates, url, views](link)
- 📁 [source code websiteku](link)

