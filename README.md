# **Sistem Prediksi Nilai Produksi Ikan yang Diekspor menggunakan metode Regresi Linier**

Berikut adalah langkah-langkah untuk membuat Sistem Prediksi Nilai Produksi Ikan yang Diekspor menggunakan metode Regresi Linier dengan bahasa pemrograman Python berdasarkan data yang diberikan:\

1. Persiapkan dataset: Dataset yang digunakan terdiri dari 4 variabel yaitu tahun, jenis ikan, produksi dalam satuan Kg, dan nilai produksi dalam satuan US $. Pastikan dataset sudah bersih dari nilai yang hilang (missing value) atau data yang tidak konsisten.
2. Memuat dataset: Muat dataset tersebut ke dalam program Python menggunakan library pandas. Gunakan fungsi pandas.read_csv() untuk memuat dataset dari file CSV.
3. Melakukan analisis deskriptif: Lakukan analisis deskriptif pada dataset, termasuk statistik dasar, seperti mean, median, dan standar deviasi untuk masing-masing variabel, serta visualisasi data untuk melihat pola yang ada.
4. Membagi dataset menjadi data latih dan data uji: Bagi dataset menjadi data latih dan data uji. Data latih digunakan untuk melatih model prediksi, sedangkan data uji digunakan untuk menguji performa model.
5. Membuat model Regresi Linier: Buat model Regresi Linier menggunakan library scikit-learn. Gunakan fungsi LinearRegression() untuk membuat model regresi linier.
6. Melatih model: Latih model menggunakan data latih yang sudah dibagi sebelumnya. Gunakan fungsi fit() pada model Regresi Linier untuk melatih model.
7. Memprediksi nilai produksi ikan: Gunakan data uji untuk memprediksi nilai produksi ikan yang diekspor. Gunakan fungsi predict() pada model Regresi Linier untuk memprediksi nilai produksi ikan.
8. Evaluasi model: Evaluasi performa model dengan menghitung nilai MSE (Mean Squared Error) dan R-Squared.\

Berikut adalah contoh kode Python untuk membuat Sistem Prediksi Nilai Produksi Ikan yang Diekspor menggunakan metode Regresi Linier:\

## Tampilan Dataset

![gambar](gambar/data1.PNG)

## Tampilan Sistem Prediksi Nilai Produksi Ikan yang Diekspor

![gambar](gambar/data2.PNG)
