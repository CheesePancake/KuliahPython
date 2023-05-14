# Modul django task 10 pdf 1 ~ 4 kelas Pemrograman Python
Untuk task ini direkomendasikan untuk melakukan instalasi dan penerapan virtualenv atau virtual environment agar modul-modul paket python global tidak bentrok

Catatan : **Seluruh Perintah / Command dibawah diketik menggunakan terminal bash**
## ⚒️ Instalasi Virtualenv
- install virtualenv dengan perintah berikut : 
```bash
$ pip install virtualenv
```
Log Bash/CMD saya seperti ini karena virtualenv sudah terinstall sebelumnya
```
$ pip install virtualenv
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: virtualenv in c:\users\u149\appdata\roaming\python\python311\site-packages (20.19.0)
Requirement already satisfied: distlib<1,>=0.3.6 in c:\users\u149\appdata\roaming\python\python311\site-packages (from virtualenv) (0.3.6)
Requirement already satisfied: filelock<4,>=3.4.1 in c:\users\u149\appdata\roaming\python\python311\site-packages (from virtualenv) (3.10.0)
Requirement already satisfied: platformdirs<4,>=2.4 in c:\users\u149\appdata\roaming\python\python311\site-packages (from virtualenv) (3.0.0)
```
## ▶️ Membuat Folder Virtualenv
- buka folder project (pada tugas ini saya namai task-10) lalu ketik perintah berikut :
```bash
$ python -m venv env
```
- munculnya folder **env** menandakan Folder telah berhasil dibuat

### 📝 Keterangan 
* **env** merupakan nama folder yang bisa di modifikasi lagi tidak harus selalu **env** misalnya `-m venv namafolder` atau jika ingin tempat folder nya ada disebuah path
maka `-m venv tempat/ke/env`

## ⏹️ Memulai dan menghentikan virtualenv
- Untuk memulai virtualenv yang sudah dibuat diatas pada **Windows** dengan **Bash** ketikkan command berikut :
```bash
$ source env/Scripts/activate
```
- aktivasi env telah berhasil jika (env) telah muncul

<img width="439" alt="image" src="https://github.com/CheesePancake/KuliahPython/assets/92983457/4ea42eef-0f73-4c98-907e-0b6db3c506f1" align="center">

- Untuk menonaktifkan ketik perintah berikut :
```bash
deactivate
```
- hilangnya (env) menandakan env telah non-aktif

## 🐍 Upgrade pip
memperbaharui package manager python bertujuan untuk mengatasi compatibility issue antara python dan modul yang ingin di install
perintah berikut digunakan untuk memperbaharui pip global maupun pip virtual environment
```bash
$ python -m pip install --upgrade pip
```
Log
```
Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3.1
    Uninstalling pip-22.3.1:
      Successfully uninstalled pip-22.3.1
Successfully installed pip-23.1.2
```

# Selanjutnya
⚒️ [Instalasi Django](link)

