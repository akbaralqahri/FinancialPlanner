# 📊 Financia - Wealth Planner Pro

Aplikasi Perencanaan Keuangan Komprehensif berbasis Python dan Streamlit untuk membantu Anda mengelola keuangan pribadi dengan lebih baik.

## ✨ Fitur Utama

### 🏠 Dashboard Utama
- **Health Score**: Penilaian kesehatan finansial secara real-time
- **Quick Stats**: Ringkasan pendapatan, pengeluaran, aset, dan hutang
- **Metrik Kesehatan**: Analisis rasio menabung, rasio hutang, dan dana darurat
- **Rekomendasi Cerdas**: Saran otomatis berdasarkan kondisi keuangan Anda
- **Analisis Cashflow**: Visualisasi arus kas bulanan

### 💰 Budget & Alokasi
- **50/30/20 Rule**: Metode budgeting klasik yang seimbang
  - 50% untuk Kebutuhan (Needs)
  - 30% untuk Keinginan (Wants)
  - 20% untuk Tabungan (Savings)
- **6 Jars System**: Metode T. Harv Eker untuk manajemen presisi
  - Living (55%), Freedom (10%), Education (10%)
  - Long Term (10%), Play (10%), Give (5%)
- **Tips Anggaran**: Panduan praktis untuk pengelolaan budget

### 🎯 Tujuan Keuangan
- Kelola multiple tujuan finansial (menikah, rumah, pendidikan, dll)
- Tracking progress setiap tujuan
- Kalkulasi otomatis kebutuhan tabungan bulanan
- Kalkulator sederhana untuk perencanaan cepat

### 🛡️ Dana Darurat
- Target dana darurat berdasarkan status pernikahan:
  - Lajang: 6 bulan pengeluaran
  - Menikah: 9 bulan pengeluaran
  - Menikah + Anak: 12 bulan pengeluaran
- Visualisasi progress dengan gauge chart
- Rekomendasi alokasi dana darurat:
  - 30% Tabungan Bank (akses instan)
  - 50% Reksadana Pasar Uang (return lebih tinggi)
  - 20% Emas/Cash (anti inflasi)

### 📉 Kalkulator Hutang
- Input multiple hutang dengan detail lengkap
- Simulasi 2 strategi pelunasan:
  - **Snowball Method**: Bayar hutang terkecil dulu (motivasi psikologis)
  - **Avalanche Method**: Bayar bunga tertinggi dulu (hemat matematis)
- Perbandingan timeline dan total bunga kedua metode
- Visualisasi proyeksi sisa hutang
- Rekomendasi strategi terbaik

### 🔥 Simulasi FIRE
- Proyeksi menuju Financial Independence Retire Early
- Target berdasarkan 4% Withdrawal Rule (25x pengeluaran tahunan)
- Visualisasi pertumbuhan aset dengan parameter:
  - Inflasi tahunan
  - Return investasi
- Kalkulasi passive income saat pensiun
- Timeline chart interaktif

### ⚙️ Pengaturan
- **Profil**: Kelola data pribadi (usia, profil risiko)
- **Data Management**: Export/Import data dalam format JSON
- **Advanced Parameters**: Sesuaikan asumsi inflasi dan return investasi

## 🚀 Cara Instalasi

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone atau download project ini**
```bash
git clone <repository-url>
cd financial-planner
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi**
```bash
streamlit run financial_planner.py
```

4. **Buka browser**
Aplikasi akan otomatis terbuka di browser pada alamat:
```
http://localhost:8501
```

## 📖 Cara Penggunaan

### 1. Setup Awal
- Buka aplikasi di browser
- Masuk ke menu "Dashboard Utama"
- Input data keuangan dasar Anda:
  - Pendapatan bulanan
  - Pengeluaran bulanan
  - Tabungan saat ini
  - Status pernikahan

### 2. Kelola Budget
- Pilih menu "Budget & Alokasi"
- Lihat breakdown budget menurut 50/30/20 Rule atau 6 Jars System
- Sesuaikan dengan preferensi Anda

### 3. Tambah Tujuan Keuangan
- Pilih menu "Tujuan Keuangan"
- Klik "Tambah Tujuan Baru"
- Input nama tujuan, target dana, dan tahun deadline
- Sistem akan menghitung kebutuhan tabungan bulanan otomatis

### 4. Cek Dana Darurat
- Pilih menu "Dana Darurat"
- Lihat progress dana darurat Anda
- Ikuti rekomendasi alokasi yang diberikan

### 5. Simulasi Pelunasan Hutang
- Pilih menu "Kalkulator Hutang"
- Input semua hutang Anda dengan detail
- Set budget bulanan untuk pelunasan
- Bandingkan strategi Snowball vs Avalanche
- Pilih strategi yang paling cocok

### 6. Proyeksi FIRE
- Pilih menu "Simulasi FIRE"
- Lihat proyeksi pertumbuhan aset Anda
- Adjust parameter inflasi dan return investasi
- Lihat kapan Anda bisa mencapai financial independence

## 🎨 Fitur Teknis

### Teknologi yang Digunakan
- **Streamlit**: Framework untuk web app Python
- **Pandas**: Data manipulation dan analysis
- **NumPy**: Numerical computing
- **Plotly**: Interactive charts dan visualisasi

### Perhitungan & Algoritma

#### Health Score (Skor Kesehatan Finansial)
```
Total Score = Savings Rate Score (40) + Debt Ratio Score (30) + Emergency Fund Score (30)

- Savings Rate: (Income - Expenses) / Income * 100
  - ≥20%: 40 poin
  - ≥10%: 20 poin
  
- Debt Ratio: Min Debt Payment / Income * 100
  - ≤30%: 30 poin
  - ≤40%: 15 poin
  
- Emergency Fund: Current Savings / Target * 100
  - ≥100%: 30 poin
  - ≥50%: 15 poin
```

#### FIRE Number Calculation
```
FIRE Number = (Monthly Expenses × 12) × 25
Passive Income = FIRE Number × 4% ÷ 12
```

#### Debt Payoff Simulation
```
Snowball: Sort debts by balance (smallest first)
Avalanche: Sort debts by interest rate (highest first)

For each month until all debts paid:
  1. Pay minimum on all debts
  2. Apply extra budget to target debt
  3. Track total interest paid
```

## 💡 Tips Penggunaan

1. **Update Data Rutin**: Update data keuangan Anda setiap bulan untuk tracking yang akurat
2. **Export Backup**: Secara berkala export data Anda sebagai backup
3. **Review Health Score**: Perhatikan Health Score dan ikuti rekomendasi yang diberikan
4. **Prioritas**: Fokus dulu pada dana darurat sebelum investasi agresif
5. **Realistic Goals**: Set tujuan yang realistis dan achievable

## 🔒 Keamanan & Privacy

- Semua data disimpan **lokal** di komputer Anda
- Tidak ada data yang dikirim ke server eksternal
- Anda memiliki kontrol penuh atas data Anda
- Export/Import data dalam format JSON yang bisa Anda backup sendiri

## 🤝 Kontribusi

Aplikasi ini adalah open source. Kontribusi dalam bentuk:
- Bug reports
- Feature requests
- Pull requests
- Feedback dan saran

sangat diterima!

## 📄 Lisensi

MIT License - Bebas digunakan untuk keperluan pribadi maupun komersial.

## 📞 Support

Jika mengalami kendala atau punya pertanyaan:
1. Baca dokumentasi ini dengan seksama
2. Cek FAQ di bawah
3. Buat issue di repository

## ❓ FAQ

**Q: Apakah data saya aman?**
A: Ya, semua data disimpan lokal di komputer Anda. Tidak ada koneksi ke server eksternal.

**Q: Bisakah saya menggunakan ini di smartphone?**
A: Ya, buka browser di smartphone dan akses localhost:8501 (jika running di network yang sama).

**Q: Bagaimana cara backup data?**
A: Gunakan fitur Export di menu Pengaturan untuk download data dalam format JSON.

**Q: Apakah bisa multi-currency?**
A: Saat ini hanya support Rupiah (IDR), tapi Anda bisa modifikasi kode untuk currency lain.

**Q: Bagaimana akurasi perhitungan?**
A: Perhitungan menggunakan formula standar financial planning. Namun ini hanya proyeksi, realita bisa berbeda.

## 🎯 Roadmap

Fitur yang akan datang:
- [ ] Multi-currency support
- [ ] Integration dengan bank (Open Banking)
- [ ] Mobile app version
- [ ] Reminder & notification
- [ ] Report generation (PDF)
- [ ] Portfolio tracker
- [ ] Tax calculator
- [ ] Retirement planning advanced

---

**Happy Planning! 💰📊**

Dibuat dengan ❤️ menggunakan Python & Streamlit
