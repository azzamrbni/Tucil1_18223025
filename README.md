# Queen Solver

<img width="390" height="390" alt="queens" src="https://github.com/user-attachments/assets/3fe6dd56-0b12-4e80-9f08-5b4937aedfb2" />

Permainan Queens dimulai dengan sebuah papan persegi kosong dengan berbagai daerah warna. Pemain diharuskan untuk menempatkan queen sehingga terdapat hanya satu queen pada tiap baris, kolom, dan daerah warna. Selain itu, satu queen tidak dapat ditempatkan bersebelahan dengan queen lainnya, termasuk secara diagonal.
Tugas ini mengharuskan pencarian solusi menggunakan algoritma brute force, yaitu mencoba semua kemungkinan penempatan queen hingga solusi yang memenuhi semua syarat ditemukan. 

Algoritma brute force yang saya gunakan disini berbasis permutasi. Secara singkat, berikut adalah urutan penyelesaiannya:
- Inisiasi brute force (membuat permutasi awal dan memulai pencarian)
- Cek validitas (tidak boleh ada queen dalam satu warna dan tidak boleh ada queen yang bertetangga secara diagonal)
- Jika valid, solusi ditemukan
- Jika tidak valid, maka dibuat permutasi baru untuk dicek kembali

Kompleksitas waktu keseluruhan algoritma adalah O(n! · n), sedangkan kompleksitas ruang adalah O(n²).

## Instalasi

### Windows/Linux/Mac
Pastikan Python 3 telah terinstall. Unduh dari https://www.python.org/downloads/

## Cara Menjalankan Program

### 1. Menjalankan Langsung
Dari direktori root proyek, jalankan dengan perintah:

```bash
python src/queensolver.py
```

### 2. Cara Mudah (Windows)
Gunakan perintah berikut:

```bash
./bin/run.bat
```

## Input dan Output

### Input
Program menerima input melalui file teks (.txt) yang berisi papan catur berbentuk grid NxN, di mana setiap sel berisi karakter yang menunjukkan area.

- Karakter yang sama menunjukkan area yang sama.
- Queen tidak boleh ditempatkan pada area yang sama.

### Output
- **GUI**: Menampilkan papan dengan penempatan queen (ditandai dengan #), dengan warna berbeda untuk setiap area.
- **Gambar**: Solusi dapat disimpan sebagai file gambar PNG.
- **TXT File**: Solusi dapat disimpan sebagai file teks.

## File Input
Lihat contoh pada folder `test/`. Contoh format:

```
AAABB
ACCCB
ACDDB
EEEFF
EFFFF
```

## Usage
1. Jalankan program.
2. Klik "Load" dan pilih file input (.txt) dari folder test.
3. Klik "Solve" untuk mencari solusi.
4. Gunakan "Save Image" atau "Save Text" untuk menyimpan hasil.

## Author
Nama | NIM | Kelas
---|---|---
Muhammad Azzam Robbani | 18223025 | STI

