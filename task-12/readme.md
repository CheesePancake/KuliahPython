# Hasil praktek task 12 pemrograman python

berikut ini adalah hasil akhir dari praktek django pada [task 10](https://github.com/CheesePancake/KuliahPython/tree/main/task-10), [task 11](https://github.com/CheesePancake/KuliahPython/tree/main/task-11) dan [task 12](https://github.com/CheesePancake/KuliahPython/tree/main/task-12)

## ⚒️ Instalasi lokal
- Clone repositori ini
- Import database yang disediakan dan sesuaikan setting.py
- Buat sebuah [virtual environment di folder root](https://github.com/CheesePancake/KuliahPython/tree/main/task-10#%EF%B8%8F-membuat-folder-virtualenv)
- Install python package yang berada didalam file requirement.txt dengan perintah berikut

```bash
$ pip install -r requirements.txt
```
- Jalankan djangoapp dengan perintah berikut :
``` bash
$ py manage.py runserver
```
yang apabila benar terminal log nya akan mirip seperti berikut :
```bash
(env) 
-@PCkau MINGW64 /d/Kuliah/Pemrograman-python/tasks/task-10/websiteku
$ py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 21, 2023 - 20:34:11
Django version 4.2.1, using settings 'websiteku.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## 🔐User Password
Gunakan akun-akun berikut untuk masuk ke dashboard django admin
| **User** 	| **Password**   	| **Keterangan**              	|
|----------	|----------------	|-----------------------------	|
| admin    	| admin          	| akun super admin            	|
| admin_2  	| officeadmin123 	| akun admin Front End Office 	|
| admin_3  	| libadmin123    	| akun admin pustakawan       	|

## 📝 Tugas dari modul
```
Buatlah tampilan Halaman Admin pada model buku berelasi dengan kategori yang telah 
disesuaikan
```
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/40d2b976-0f99-47a1-b8fd-9fb436b2f0a2">

## 🚀 Menyesuaikan versi django-jet
Dalam tugas ini saya menggunakan [Django-Jet2](https://pypi.org/project/django-jet2/) yang kompatibel dengan versi python 3.11 dan django 4.2.1 yang saya gunakan untuk mengikuti materi didalam modul 10 hingga 12

<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/7d22544d-b2a7-4e44-8c46-cca3b34b3f70">
<br>
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/28248fb1-a891-4794-b598-5728ea166393">

## 🖼️ Tampilan Akhir 'websiteku'
Berikut tampilan-tampilan akhir dari halaman 'websiteku' setelah saya mengerjakan tugas ini

<img width="959" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/bbbcd76a-3eaf-449a-abb1-72322130c43e">
<br>
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/13dc2f6d-8c3f-4306-829c-9b986e596e20">
<br>
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/129599bb-8fe2-430c-b689-b33de0f5d88a">
<br>
<img width="960" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/d0f7cc6b-2d92-4226-99e5-8e31ee5b6879">




