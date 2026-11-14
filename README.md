# BaliVoy Media & Document Assets CDN 🌴

Repository publik resmi untuk hosting aset media statis, video latar berkecepatan tinggi, dan file unduhan PDF e-booklet pariwisata **BaliVoy**.

Dengan memisahkan aset ini ke repository publik GitHub, seluruh konsumsi kuota bandwidth dan storage **Firebase tetap 100% hemat dan bebas biaya**, sementara pengunjung website mendapatkan kecepatan unduhan maksimal melalui jaringan CDN global **jsDelivr** & **GitHub Raw**.

---

## 📁 Struktur Direktori

```text
balivoy-assets/
├── videos/             # Video latar belakang web (MP4 / WebM terkompresi)
│   └── .gitkeep
├── images/             # Gambar latar hero & poster resolusi tinggi (WebP)
│   └── .gitkeep
└── pdf/                # Buku panduan wisata & kalender event (PDF)
    └── .gitkeep
```

---

## ⚡ URL CDN Siap Pakai

File yang diunggah ke branch `main` dapat diakses langsung menggunakan URL CDN berikut:

### 1. jsDelivr Edge CDN (Direkomendasikan untuk Website Cepat)
- **Video:** `https://cdn.jsdelivr.net/gh/Patiank/balivoy-assets@main/videos/<nama-video>.mp4`
- **PDF E-Booklet:** `https://cdn.jsdelivr.net/gh/Patiank/balivoy-assets@main/pdf/<nama-file>.pdf`
- **Gambar:** `https://cdn.jsdelivr.net/gh/Patiank/balivoy-assets@main/images/<nama-gambar>.webp`

*Fitur: HTTP/2, HTTP/3, Multi-CDN failover global, otomatis dicache di edge server terdekat dengan pengunjung.*

### 2. GitHub Raw Direct
- `https://raw.githubusercontent.com/Patiank/balivoy-assets/main/<folder>/<nama-file>`

---

## 🎬 Standar Optimasi Video Web
- **Format:** MP4 (`libx264` / AAC atau tanpa audio)
- **Flag Web Streaming:** `-movflags +faststart` (agar video langsung berputar tanpa menunggu download selesai)
- **Target Ukuran:** 2 MB – 5 MB (durasi 10 – 20 detik looping)
