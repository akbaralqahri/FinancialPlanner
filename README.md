# 📊 Financial Planner Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Aplikasi perencanaan keuangan pribadi yang komprehensif dan interaktif**

[Demo](#demo) • [Fitur](#fitur) • [Instalasi](#instalasi) • [Penggunaan](#penggunaan) • [Teknologi](#teknologi)

</div>

---

## 📖 Deskripsi

Financial Planner Dashboard adalah aplikasi web berbasis Streamlit yang dirancang untuk membantu Anda mengelola keuangan pribadi dengan lebih baik. Aplikasi ini menyediakan berbagai fitur mulai dari manajemen budget, pelunasan hutang, perencanaan tujuan keuangan, hingga simulasi FIRE (Financial Independence Retire Early).

Dengan antarmuka yang modern dan intuitif, Anda dapat dengan mudah memvisualisasikan kondisi keuangan Anda, membuat proyeksi masa depan, dan mendapatkan rekomendasi cerdas untuk mencapai kebebasan finansial.

---

## ✨ Fitur

### 🏠 Dashboard Utama
- **Health Score Finansial**: Penilaian otomatis kondisi keuangan Anda (0-100)
- **Quick Stats**: Ringkasan pendapatan, pengeluaran, aset, dan hutang
- **Rekomendasi Cerdas**: Saran prioritas berdasarkan kondisi keuangan
- **Visualisasi Cashflow**: Grafik interaktif analisis arus kas bulanan
- **Metrik Kesehatan**: Monitoring rasio menabung, rasio hutang, dan dana darurat

### 💰 Budget & Alokasi
- **50/30/20 Rule**: Metode klasik untuk pembagian anggaran
  - 50% Kebutuhan (Needs)
  - 30% Keinginan (Wants)
  - 20% Tabungan (Savings)
- **6 Jars System**: Metode T. Harv Eker untuk manajemen presisi
  - Living (55%), Freedom (10%), Education (10%)
  - Long Term Savings (10%), Play (10%), Give (5%)
- **Kalkulator Alokasi**: Perhitungan otomatis berdasarkan pendapatan

### 🎯 Tujuan Keuangan
- **Manajemen Goals**: Tambah, edit, dan hapus tujuan keuangan
- **Progress Tracking**: Monitor perkembangan setiap tujuan
- **Kalkulator Cepat**: Hitung kebutuhan menabung untuk mencapai target
- **Timeline Visualization**: Visualisasi waktu pencapaian tujuan
- **Rekomendasi Bulanan**: Saran alokasi dana per bulan

### 🛡️ Dana Darurat
- **Target Otomatis**: Perhitungan berdasarkan status pernikahan
  - Lajang: 6 bulan pengeluaran
  - Menikah: 9 bulan pengeluaran
  - Menikah + Anak: 12 bulan pengeluaran
- **Gauge Visualization**: Tampilan visual kesiapan dana darurat
- **Strategi Alokasi**: Rekomendasi pembagian di berbagai instrumen
  - 30% Tabungan Bank (likuiditas tinggi)
  - 50% Reksadana Pasar Uang (return optimal)
  - 20% Emas/Cash (lindung nilai inflasi)

### 📉 Kalkulator Hutang
- **Manajemen Hutang**: Track multiple hutang dengan detail lengkap
- **Dual Strategy Simulator**:
  - **Snowball Method**: Bayar hutang terkecil dulu (motivasi psikologis)
  - **Avalanche Method**: Bayar bunga tertinggi dulu (efisiensi matematis)
- **Perbandingan Timeline**: Grafik proyeksi pelunasan kedua metode
- **Total Interest Calculation**: Perhitungan total bunga yang harus dibayar
- **Rekomendasi Optimal**: Saran metode terbaik untuk kondisi Anda

### 🔥 Simulasi FIRE
- **FIRE Calculator**: Hitung target kebebasan finansial
- **25x Rule**: Target aset = 25x pengeluaran tahunan
- **4% Withdrawal Rule**: Strategi penarikan dana yang sustainable
- **Proyeksi Pertumbuhan**: Grafik proyeksi aset hingga 30 tahun
- **Parameter Customizable**: Sesuaikan asumsi inflasi dan return investasi
- **Passive Income Projection**: Estimasi pendapatan pasif saat FIRE

### ⚙️ Pengaturan
- **Profil Pengguna**: Kelola data pribadi dan profil risiko
- **Export/Import Data**: Backup dan restore data dalam format JSON
- **Parameter Advanced**: Kustomisasi asumsi inflasi dan return investasi
- **Data Summary**: Ringkasan lengkap semua metrik finansial

---

## 🚀 Instalasi

### Prerequisites

Pastikan Anda sudah menginstall:
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository**
```bash
git clone <repository-url>
cd financial-planner-dashboard
```

2. **Buat virtual environment (opsional tapi disarankan)**
```bash
python -m venv venv

# Aktivasi virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Jalankan aplikasi**
```bash
streamlit run app.py
```

5. **Akses aplikasi**
Buka browser dan akses: `http://localhost:8501`

---

## 📦 Dependencies

Aplikasi ini menggunakan library berikut:

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
```

Untuk install semua dependencies:
```bash
pip install streamlit pandas numpy plotly
```

---

## 💻 Penggunaan

### 1. Setup Awal

Saat pertama kali membuka aplikasi:
1. Masukkan data pendapatan bulanan Anda
2. Input pengeluaran bulanan rata-rata
3. Tambahkan tabungan/aset yang sudah dimiliki
4. Pilih status pernikahan (single/married/married with kids)

### 2. Input Hutang

Di menu **Kalkulator Hutang**:
1. Klik "Tambah Hutang Baru"
2. Masukkan detail hutang (nama, sisa pokok, bunga, pembayaran minimum)
3. Tetapkan budget bulanan untuk pelunasan
4. Lihat simulasi perbandingan metode Snowball vs Avalanche

### 3. Set Tujuan Keuangan

Di menu **Tujuan Keuangan**:
1. Klik "Tambah Tujuan Baru"
2. Beri nama tujuan (contoh: "Beli Mobil", "DP Rumah")
3. Set target dana dan tahun pencapaian
4. Input dana yang sudah terkumpul
5. Monitor progress secara berkala

### 4. Simulasi FIRE

Di menu **Simulasi FIRE**:
1. Review parameter investasi (inflasi dan return)
2. Lihat proyeksi pertumbuhan aset
3. Cek kapan Anda bisa mencapai FIRE number
4. Adjust lifestyle expenses untuk mempercepat FIRE

### 5. Export Data

Di menu **Pengaturan**:
1. Pilih tab "Manajemen Data"
2. Klik "Download Data (JSON)"
3. Simpan file backup di tempat aman
4. Gunakan untuk restore jika diperlukan

---

## 🎨 Fitur UI/UX

### Dark Mode Design
- Tema gelap modern dengan gradien warna cerah
- High contrast untuk readability optimal
- Glassmorphism effects pada card components

### Interactive Components
- Hover effects pada semua card dan button
- Smooth transitions dan animations
- Responsive layout untuk berbagai ukuran layar

### Data Visualization
- Interactive charts dengan Plotly
- Real-time updates pada metric cards
- Progress bars dengan color coding

### Custom Styling
- Plus Jakarta Sans font family
- Gradient backgrounds dan borders
- Consistent color scheme (purple-pink gradient)

---

## 📊 Metodologi & Konsep

### Financial Health Score

Skor dihitung berdasarkan 3 faktor utama:

1. **Savings Rate (40 poin)**
   - ≥20%: 40 poin
   - 10-20%: 20 poin
   - <10%: 0 poin

2. **Debt Ratio (30 poin)**
   - ≤30%: 30 poin
   - 30-40%: 15 poin
   - >40%: 0 poin

3. **Emergency Fund (30 poin)**
   - ≥100%: 30 poin
   - 50-100%: 15 poin
   - <50%: 0 poin

**Interpretasi:**
- 80-100: Sangat Sehat 🟢
- 50-80: Cukup Sehat 🟡
- 0-50: Perlu Perhatian 🔴

### FIRE Calculation

**Formula:**
- FIRE Number = Annual Expenses × 25
- Safe Withdrawal Rate = 4% per tahun
- Passive Income = FIRE Number × 4% ÷ 12 bulan

**Asumsi:**
- Return investasi: 8% per tahun (real return setelah inflasi)
- Inflasi: 4% per tahun
- Portfolio: Mix saham dan obligasi

### Debt Payoff Strategies

**Snowball Method:**
- Prioritas: Hutang dengan saldo terkecil
- Keuntungan: Motivasi psikologis (quick wins)
- Cocok untuk: Yang butuh motivasi extra

**Avalanche Method:**
- Prioritas: Hutang dengan bunga tertinggi
- Keuntungan: Hemat bunga maksimal
- Cocok untuk: Yang fokus pada efisiensi matematis

---

## 🔒 Keamanan Data

- **Local Storage**: Semua data disimpan di session state (tidak ada database)
- **No Cloud Sync**: Data tidak dikirim ke server eksternal
- **Privacy First**: Tidak ada tracking atau analytics
- **Export/Import**: User punya kontrol penuh atas data mereka

⚠️ **Catatan**: Data akan hilang saat refresh browser. Gunakan fitur export untuk backup!

---

## 🛠️ Customization

### Mengubah Tema Warna

Edit bagian CSS di file utama:

```python
# Gradient utama (purple-pink)
background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%)

# Ganti dengan warna favorit Anda
background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%)
```

### Menambah Metode Budget Baru

Tambahkan di menu "Budget & Alokasi":

```python
allocations_custom = [
    {'label': 'Category Name', 'pct': 50, 'color': '#hexcolor', 
     'desc': 'Description', 'icon': '🎯'}
]
```

### Custom Financial Goals

Modifikasi struktur goals di session state:

```python
{
    'id': unique_id,
    'name': 'Goal Name',
    'target': target_amount,
    'current': current_amount,
    'deadline_year': year,
    'priority': 'high/medium/low'  # custom field
}
```

---

## 📱 Screenshots

### Dashboard Utama
- Health score badge dengan gauge indicator
- Quick stats cards (income, expenses, assets, debts)
- Cashflow visualization chart
- Smart recommendations

### Debt Calculator
- Dual strategy comparison (Snowball vs Avalanche)
- Interactive timeline projection
- Total interest savings calculation
- Debt management interface

### FIRE Simulator
- Asset growth projection chart
- FIRE number calculation
- Passive income estimation
- Customizable parameters

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

### Area yang Bisa Dikembangkan

- [ ] Multi-currency support
- [ ] Integration dengan API bank
- [ ] Machine learning untuk expense categorization
- [ ] Mobile app version
- [ ] Database integration untuk persistence
- [ ] Investment portfolio tracker
- [ ] Tax calculator Indonesia
- [ ] Bill reminder notifications
- [ ] Multi-language support (EN, ID)
- [ ] Dark/Light theme toggle

---

## 📄 License

Project ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

---

## 👨‍💻 Author & Copyright

**Muhammad Ali Akbar Al - Qahri**

© 2026 @akbaralqahri. All rights reserved.

### Connect with me:

- 💼 [LinkedIn](https://www.linkedin.com/in/akbaralqahri/)
- 🌐 [Portfolio](https://akbaralqahri.github.io/portofolio/)

---

## 🙏 Acknowledgments

- Streamlit team untuk framework yang luar biasa
- Plotly untuk library visualisasi data
- T. Harv Eker untuk konsep 6 Jars System
- FIRE community untuk inspirasi dan metodologi
- Indonesian finance community untuk feedback

---

## 📞 Support

Jika Anda menemukan bug atau punya saran fitur:

1. Buka [Issues](../../issues) di GitHub
2. Hubungi via [LinkedIn](https://www.linkedin.com/in/akbaralqahri/)
3. Email: [contact via portfolio site](https://akbaralqahri.github.io/portofolio/)

---

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication system
- [ ] Cloud backup & sync
- [ ] Mobile responsive design improvements
- [ ] Advanced investment calculator
- [ ] Retirement planning module

### Version 2.5 (Future)
- [ ] AI-powered financial advisor
- [ ] Automatic expense categorization
- [ ] OCR for receipt scanning
- [ ] Integration with Indonesian banks
- [ ] Crypto portfolio tracking
- [ ] Real estate investment calculator

---

## 📚 Referensi & Bacaan

### Buku
- "The Secrets of the Millionaire Mind" - T. Harv Eker
- "Your Money or Your Life" - Vicki Robin & Joe Dominguez
- "The Simple Path to Wealth" - JL Collins

### Website
- [Mr. Money Mustache](https://www.mrmoneymustache.com/)
- [Financial Independence Reddit](https://www.reddit.com/r/financialindependence/)
- [Indonesian FIRE Community](https://www.reddit.com/r/indonesiakaya/)

### Tools
- [FIRE Calculator](https://www.firecalc.com/)
- [Personal Capital](https://www.personalcapital.com/)
- [Mint](https://www.mint.com/)

---

<div align="center">

**⭐ Star this repository jika Anda merasa terbantu!**

by [@akbaralqahri](https://akbaralqahri.github.io/portofolio/)

</div>
