# PyPBEE Türkçe Web Arayüzü 🏗️

PyPBEE (Performance-Based Earthquake Engineering) için geliştirilmiş **kapsamlı Türkçe web arayüzü**.

Bu arayüz, PyPBEE'nin tüm fonksiyonlarına Türkçe dilinde kullanıcı dostu erişim sağlar.

## 🌟 Özellikler

### ✅ Tam Türkçe Destek
- Tüm arayüz elementleri Türkçe
- Türkçe parametre açıklamaları
- Türkçe hata mesajları ve yardım metinleri

### 📊 Kapsanan Tüm Fonksiyonlar
1. **🔍 Ön Analiz (Preliminary Analysis)**
   - Mod analizi
   - Temel yapısal özellikler
   - Periyot ve sönüm hesaplamaları

2. **📊 PSHA (Olasılıksal Sismik Tehlike Analizi)**
   - Sismik tehlike eğrileri
   - Deagregasyon analizleri
   - Tehlike spektrumları

3. **🌍 GMS (Yer Hareketi Seçimi)**
   - Spektral eşleştirme
   - Yer hareketi ölçeklendirme
   - Kayıt seçim parametreleri

4. **⚡ NLTHA (Doğrusal Olmayan Zaman Tanım Alanı Analizi)**
   - Dinamik analiz
   - EDP hesaplama
   - Zaman serisi analizi

5. **📈 PSDemHA (Talep Tehlike Analizi)**
   - Talep tehlike eğrileri
   - EDP-IM ilişkileri
   - Olasılıksal talep analizi

6. **🔴 PSDamHA (Hasar Tehlike Analizi)**
   - Hasar tehlike eğrileri
   - Kırılganlık fonksiyonları
   - Hasar durumu analizleri

### 📈 Görselleştirme ve Raporlama
- **Grafikler:**
  - Tehlike eğrileri
  - Spektral eşleştirme grafikleri
  - Zaman serileri
  - Kırılganlık eğrileri
  - EDP dağılımları

- **Veri İndirme:**
  - CSV formatında sonuç indirme
  - PNG formatında grafik indirme
  - Tüm analizler için export desteği

### 🎨 Kullanıcı Dostu Arayüz
- Modern, responsive tasarım
- Kolay navigasyon
- Parametrik form girişleri
- Anlık sonuç görüntüleme
- İnteraktif grafikler

## 🚀 Kurulum

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/EmreErbek/webPyPBEE.git
cd webPyPBEE
```

### 2. Sanal Ortam Oluşturun (İsteğe Bağlı ama Önerilir)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

### 3. Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

### Web Arayüzünü Başlatma

```bash
streamlit run web_interface.py
```

Tarayıcınız otomatik olarak açılacaktır. Açılmazsa, terminal çıktısındaki URL'yi (`http://localhost:8501`) tarayıcınıza yapıştırın.

### Alternatif Başlatma Scripti

```bash
python start_web_interface.py
```

## 📖 Kullanım Kılavuzu

### 1. Çalışma Dizini Ayarlama
- Sol taraftaki yan panelden çalışma dizininizi belirleyin
- "Dizin Oluştur" butonuna tıklayın
- Tüm analiz sonuçları bu dizinde saklanacaktır

### 2. Analiz Seçimi
- Üst taraftaki sekmelerden yapmak istediğiniz analizi seçin:
  - 🏠 Ana Sayfa: Genel bilgiler
  - 🔍 Ön Analiz: Mod analizi
  - 📊 PSHA: Sismik tehlike analizi
  - 🌍 GMS: Yer hareketi seçimi
  - ⚡ NLTHA: Dinamik analiz
  - 📈 PSDemHA: Talep tehlike analizi
  - 🔴 PSDamHA: Hasar tehlike analizi

### 3. Parametreleri Girin
- Her analiz türü için gerekli parametreleri girin
- Yardım simgelerine (?) tıklayarak açıklamaları görün
- Gelişmiş ayarlar için ilgili bölümleri açın

### 4. Analizi Çalıştırın
- "Analizi Çalıştır" butonuna tıklayın
- Ekranda örnek kod ve açıklamalar görüntülenecektir
- Gerçek analiz için Python kodunu çalıştırmanız gerekir

### 5. Sonuçları Görüntüleyin
- "Sonuçları Yükle" butonu ile sonuç dosyalarını bulun
- Grafikler oluşturun
- Detayları inceleyin
- CSV olarak indirin

## 📊 Örnek Kullanım Senaryosu

### Senaryo: Bir Köprünün Sismik Performans Analizi

1. **Ön Analiz:**
   - Köprü modelinizin mod şekillerini ve periyotlarını hesaplayın
   - Sonuçları CSV olarak kaydedin

2. **PSHA:**
   - Köprü konumunuz için sismik tehlike analizini çalıştırın
   - Tehlike eğrilerini görselleştirin

3. **GMS:**
   - Hedef spektruma uygun yer hareketi kayıtları seçin
   - Seçilen kayıtları CSV olarak indirin

4. **NLTHA:**
   - Seçilen kayıtlar altında dinamik analiz yapın
   - EDP değerlerini hesaplayın
   - Zaman serilerini görüntüleyin

5. **PSDemHA:**
   - Talep tehlike eğrilerini oluşturun
   - Kritik EDP değerlerini belirleyin

6. **PSDamHA:**
   - Hasar durumlarını tanımlayın
   - Kırılganlık eğrilerini çizin
   - Hasar tehlike eğrilerini analiz edin

## 🎯 Özellikler Detayları

### CSV Export
Her analiz sonucu için:
- Otomatik veri tabloları
- Tek tıkla CSV indirme
- UTF-8 kodlama (Türkçe karakter desteği)

### Grafik Export
Tüm grafikler için:
- Yüksek çözünürlük (300 DPI)
- PNG formatı
- Yayın kalitesi

### Veri Görüntüleme
- İlk N satır önizleme
- JSON formatında detay görüntüleme
- İstatistiksel özetler

## 🔧 Teknik Detaylar

### Kullanılan Teknolojiler
- **Streamlit**: Web arayüzü framework'ü
- **Pandas**: Veri işleme
- **Matplotlib**: Grafik oluşturma
- **NumPy**: Sayısal hesaplamalar
- **Pickle**: Sonuç dosyası okuma

### Sistem Gereksinimleri
- **Python**: 3.9 veya üzeri
- **RAM**: Minimum 4 GB (8 GB önerilir)
- **Disk**: 500 MB (sonuçlar hariç)
- **İşletim Sistemi**: Windows, Linux, macOS

## 📁 Dosya Yapısı

```
webPyPBEE/
│
├── web_interface.py          # Ana web arayüzü
├── requirements.txt          # Python bağımlılıkları
├── README_TR.md             # Türkçe README (bu dosya)
├── README.md                # İngilizce README
│
├── pypbee/                  # PyPBEE ana modülü
│   ├── __init__.py
│   ├── analysis.py
│   ├── psha.py
│   ├── gms.py
│   ├── nltha.py
│   ├── psdemha.py
│   ├── psdamha.py
│   └── ...
│
└── examples/                # Örnek projeler
    ├── Bridge_A/
    ├── Bridge_B/
    └── ...
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz!

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 🐛 Hata Bildirimi

Bir hata bulduysanız veya öneriniz varsa:
- GitHub Issues sayfasından yeni bir issue açın
- Hatanın detaylı açıklamasını yapın
- Ekran görüntüsü ekleyin (varsa)
- Hata mesajını paylaşın

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE.md) dosyasına bakın.

## 👥 Yazarlar

- **Orijinal PyPBEE**: Angshuman Deb
- **Türkçe Web Arayüzü**: PyPBEE Community

## 🙏 Teşekkürler

- **Caltrans** (65A0594, Task 2880)
- **PEER Transportation Systems Research Program** (Project #1147-NCTRTE)
- **Reissner Chair, UC San Diego**
- **TACC** (HPC kaynakları)

## 📞 İletişim

- **GitHub**: [https://github.com/EmreErbek/webPyPBEE](https://github.com/EmreErbek/webPyPBEE)
- **Orijinal Proje**: [https://github.com/angshuman311/PyPBEE](https://github.com/angshuman311/PyPBEE)

## 📚 Ek Kaynaklar

- [PyPBEE Dokümantasyonu](https://github.com/angshuman311/PyPBEE)
- [OpenSees](https://opensees.berkeley.edu/)
- [PEER NGA Database](https://ngawest2.berkeley.edu/)

---

**Not**: Bu web arayüzü, PyPBEE'nin tüm fonksiyonlarını kullanıcı dostu bir şekilde sunmak için geliştirilmiştir. Gerçek analizleri çalıştırmak için Python scriptlerini kullanmanız gerekmektedir. Bu arayüz, parametre girişi, sonuç görselleştirme ve veri indirme işlemlerini kolaylaştırır.

## 🎓 Akademik Kullanım

Bu yazılımı akademik çalışmalarınızda kullanıyorsanız, lütfen orijinal PyPBEE projesini kaynak gösterin:

```
Deb, A. (2024). PyPBEE: Performance-Based Earthquake Engineering in Python.
GitHub repository, https://github.com/angshuman311/PyPBEE
```

---

## ⚡ Hızlı Başlangıç

```bash
# 1. Klonla
git clone https://github.com/EmreErbek/webPyPBEE.git
cd webPyPBEE

# 2. Kurulum
pip install -r requirements.txt

# 3. Başlat
streamlit run web_interface.py
```

**Artık hazırsınız! 🎉**

Tarayıcınızda `http://localhost:8501` adresine gidin ve PyPBEE'nin Türkçe arayüzünü kullanmaya başlayın!
