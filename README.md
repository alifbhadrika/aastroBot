# aastroBot
> A task reminder bot made with Python Flask and Bootstrap

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
![Example screenshot](./img/screenshot.png)
aastroBot merupakan sebuah task reminder bot yang berfungsi untuk membantu mengingat berbagai deadline, tanggal penting, dan task-task
tertentu kepada user yang menggunakannya. Dengan memanfaatkan algoritma String Matching dan Regular Expression

## Technologies
* Python
* Flask
* Bootstrap

## Setup
*Sebelum menjalankan hal-hal dibawah, pastikan anda memiliki **Python 3.8+**, **Python3-pip**, dan juga **Python Virtual Environment***
1. Clone repository `git clone https://github.com/alifbhadrika/aastroBot.git`
2. Buat virtual environment
Windows:
```
python -m venv env
env\Scripts\activate
```
Linux/Centos/Ubuntu/MacOS:
```
python3 -m venv env
source env/bin/activate
```
3. Install requirements.txt 
Windows:
```
pip install -r requirements.txt
```
Linux/Centos/Ubuntu/MacOS:
```
python3 -m pip install -r requirements.txt
```
4. Buka folder src `cd aastroBot/src`
5. Jalankan aplikasi `python app.py`
6. Buka link yang ditampilkan pada terminal

## Features
* Menambahkan Task
* Melihat Daftar Task
* Menampilkan Deadline dari Suatu Task Tertentu
* Memperbarui Task Tertentu
* Menandai bahwa Suatu Task Sudah Selesai Dikerjakan
* Menampilkan Opsi help yang difasilitasi oleh Bot
* Menampilkan Pesan Error jika Bot Tidak Dapat Mengenali Masukan User

## Status
Project is: _finished_

## Creator
* Raihan Astrada Fathurrahman (13519113)
* Naufal Yahya Kurnianto (13519141)
* Alif Bhadrika Parikesit (13519186)
