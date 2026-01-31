# 🚀 Quick Start Guide - Financia

Panduan cepat untuk memulai menggunakan Financia - Wealth Planner Pro.

## ⚡ Instalasi Express (5 Menit)

### Windows

1. **Install Python**
   - Download dari https://python.org
   - Pastikan centang "Add Python to PATH"

2. **Buka Command Prompt**
   - Tekan `Win + R`, ketik `cmd`, Enter

3. **Install Dependencies**
   ```cmd
   pip install streamlit pandas numpy plotly
   ```

4. **Jalankan Aplikasi**
   ```cmd
   streamlit run financial_planner.py
   ```

### Mac / Linux

1. **Buka Terminal**

2. **Install Dependencies**
   ```bash
   pip3 install streamlit pandas numpy plotly
   ```

3. **Jalankan Aplikasi**
   ```bash
   streamlit run financial_planner.py
   ```

## 📋 Checklist Setup Awal

- [ ] Install Python 3.8+
- [ ] Install dependencies (streamlit, pandas, numpy, plotly)
- [ ] Jalankan aplikasi
- [ ] Buka http://localhost:8501 di browser
- [ ] Input data keuangan dasar Anda
- [ ] Explore fitur-fitur yang tersedia

## 🎯 Tutorial 10 Menit

### Langkah 1: Dashboard (2 menit)
1. Buka aplikasi
2. Lihat Health Score Anda (default data)
3. Update pendapatan & pengeluaran bulanan
4. Update tabungan saat ini
5. Pilih status pernikahan

### Langkah 2: Budget (2 menit)
1. Klik menu "Budget & Alokasi"
2. Lihat breakdown 50/30/20 Rule
3. Bandingkan dengan 6 Jars System
4. Catat alokasi yang cocok untuk Anda

### Langkah 3: Tujuan (2 menit)
1. Klik menu "Tujuan Keuangan"
2. Edit tujuan default atau tambah baru
3. Set target dana dan deadline
4. Lihat perhitungan tabungan bulanan

### Langkah 4: Dana Darurat (2 menit)
1. Klik menu "Dana Darurat"
2. Lihat target dana darurat Anda
3. Check progress saat ini
4. Ikuti rekomendasi alokasi

### Langkah 5: FIRE (2 menit)
1. Klik menu "Simulasi FIRE"
2. Lihat proyeksi keuangan Anda
3. Adjust parameter inflasi & return
4. Lihat kapan bisa pensiun dini

## 💡 Tips Cepat

### Untuk Pemula
- Mulai dari Dashboard, input data yang akurat
- Fokus dulu ke Dana Darurat sebelum investasi
- Gunakan 50/30/20 Rule untuk budgeting awal
- Set minimal 1 tujuan jangka pendek (1-2 tahun)

### Untuk User Berpengalaman
- Gunakan 6 Jars System untuk kontrol lebih detail
- Explore Kalkulator Hutang jika punya cicilan
- Simulasikan berbagai skenario di FIRE
- Export data secara berkala untuk backup

### Untuk Investor
- Set parameter return sesuai portfolio Anda
- Adjust inflasi berdasarkan target investasi
- Gunakan FIRE calculator untuk target pensiun
- Track progress setiap bulan

## 🔧 Troubleshooting Cepat

### Aplikasi tidak mau jalan?
```bash
# Cek versi Python
python --version  # Harus 3.8+

# Install ulang dependencies
pip install -r requirements.txt --upgrade

# Jalankan lagi
streamlit run financial_planner.py
```

### Port sudah digunakan?
```bash
# Gunakan port lain
streamlit run financial_planner.py --server.port 8502
```

### Data hilang?
- Data tersimpan di session browser
- Jika refresh/close, data akan reset
- Gunakan Export untuk backup permanent

## 📊 Sample Use Cases

### Case 1: Fresh Graduate (Gaji 8 Juta)
```
Pendapatan: Rp 8.000.000
Pengeluaran: Rp 5.000.000
Tabungan: Rp 10.000.000
Status: Single

Target:
1. Dana Darurat: Rp 30.000.000 (6 bulan)
2. DP Motor: Rp 5.000.000 (1 tahun)
3. Dana Nikah: Rp 50.000.000 (3 tahun)
```

### Case 2: Karyawan Senior (Gaji 20 Juta)
```
Pendapatan: Rp 20.000.000
Pengeluaran: Rp 12.000.000
Tabungan: Rp 100.000.000
Status: Married

Target:
1. Dana Darurat: Rp 108.000.000 (9 bulan) ✓
2. DP Rumah: Rp 200.000.000 (2 tahun)
3. Dana Pendidikan Anak: Rp 500.000.000 (10 tahun)

Hutang:
- KPR: Rp 500.000.000 (bunga 8%)
```

### Case 3: Pengusaha (Income Variabel)
```
Pendapatan: Rp 50.000.000 (rata-rata)
Pengeluaran: Rp 25.000.000
Tabungan: Rp 500.000.000
Status: Married with Kids

Target:
1. Dana Darurat: Rp 300.000.000 (12 bulan) ✓
2. FIRE: Rp 7.500.000.000 (15 tahun)
3. Warisan Anak: Rp 2.000.000.000 (20 tahun)
```

## 🎓 Resources Tambahan

### Belajar Financial Planning
- Buku: "Rich Dad Poor Dad" - Robert Kiyosaki
- Buku: "The Richest Man in Babylon" - George S. Clason
- YouTube: Felicia Putri Tjiasaka, QM Financial
- Podcast: Finansialku, Ternak Uang

### Investasi Pemula
- Reksadana: Bareksa, Bibit, Tanamduit
- Saham: Stockbit, RTI Business, Indo Premier
- P2P Lending: Akseleran, Investree
- Crypto: Indodax, Tokocrypto (high risk!)

### Community
- Telegram: Investor Saham Pemula Indonesia
- Facebook: Komunitas Finansialku
- Reddit: r/finansial

## ✅ Next Steps

Setelah setup dan familiar dengan aplikasi:

1. **Minggu 1**: Input data akurat, set semua goals
2. **Minggu 2-4**: Track pengeluaran harian, update data
3. **Bulan 2**: Review progress, adjust budget
4. **Bulan 3**: Evaluasi strategi, optimize alokasi
5. **Ongoing**: Update rutin, eksperimen berbagai skenario

---

**Selamat merencanakan masa depan finansial Anda! 🚀💰**

Ada pertanyaan? Baca FAQ di README.md atau buat issue di repository.
