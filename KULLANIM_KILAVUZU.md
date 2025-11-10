# PyPBEE Türkçe Web Arayüzü - Kullanım Kılavuzu 📖

## İçindekiler
1. [Giriş](#giriş)
2. [Hızlı Başlangıç](#hızlı-başlangıç)
3. [Ana Sayfa](#ana-sayfa)
4. [Ön Analiz](#ön-analiz)
5. [PSHA Analizi](#psha-analizi)
6. [GMS - Yer Hareketi Seçimi](#gms---yer-hareketi-seçimi)
7. [NLTHA Analizi](#nltha-analizi)
8. [PSDemHA - Talep Tehlike Analizi](#psdemha---talep-tehlike-analizi)
9. [PSDamHA - Hasar Tehlike Analizi](#psdamha---hasar-tehlike-analizi)
10. [Sonuç İndirme ve Export](#sonuç-indirme-ve-export)
11. [Sık Sorulan Sorular](#sık-sorulan-sorular)
12. [Sorun Giderme](#sorun-giderme)

---

## Giriş

PyPBEE Türkçe Web Arayüzü, Performance-Based Earthquake Engineering (PBEE) analizlerini kullanıcı dostu bir şekilde gerçekleştirmenizi sağlar. Bu kılavuz, arayüzün tüm özelliklerini detaylı olarak açıklar.

### Arayüz Bileşenleri

```
┌─────────────────────────────────────────────────────────┐
│  🏗️ PyPBEE - Ana Başlık                                 │
├─────────────┬───────────────────────────────────────────┤
│             │  [Ana Sayfa] [Ön Analiz] [PSHA] [GMS]    │
│  Sol Panel  │  [NLTHA] [PSDemHA] [PSDamHA]              │
│             │                                            │
│  - Proje    │  ┌──────────────────────────────────┐    │
│    Bilgileri│  │                                  │    │
│  - Çalışma  │  │  Ana İçerik Alanı                │    │
│    Dizini   │  │                                  │    │
│  - Hakkında │  │  (Parametreler, Grafikler,       │    │
│  - Modüller │  │   Sonuçlar)                      │    │
│             │  │                                  │    │
│             │  └──────────────────────────────────┘    │
└─────────────┴───────────────────────────────────────────┘
```

---

## Hızlı Başlangıç

### 1. Kurulum

```bash
# Gerekli paketleri yükle
pip install -r requirements.txt
```

### 2. Başlatma

**Yöntem 1: Doğrudan Streamlit**
```bash
streamlit run web_interface.py
```

**Yöntem 2: Başlatıcı Script**
```bash
python start_web_interface.py
```

### 3. İlk Kullanım

1. Tarayıcınızda `http://localhost:8501` açılacak
2. Sol panelden çalışma dizininizi ayarlayın
3. "Dizin Oluştur" butonuna tıklayın
4. İstediğiniz analiz sekmesine geçin
5. Parametreleri girin ve analizi çalıştırın

---

## Ana Sayfa

### Neler Var?

**Sol Kolon:**
- PyPBEE hakkında genel bilgi
- Ana özellikler listesi
- Framework'ün avantajları

**Sağ Kolon:**
- Analiz aşamalarının açıklamaları
- Her modülün ne yaptığı
- İş akışı özeti

**Alt Bölüm:**
- Hızlı başlangıç adımları
- Temel kullanım talimatları

### Kullanım İpuçları

💡 **İpucu 1**: Ana sayfayı ilk kez kullanırken okumanızı öneririz.

💡 **İpucu 2**: Her analiz türünün açıklamasını dikkatlice okuyun.

---

## Ön Analiz

### Ne İşe Yarar?

Ön analiz, yapısal modelin temel dinamik özelliklerini belirler:
- Mod şekilleri
- Doğal periyotlar
- Sönüm oranları
- Mod katkı faktörleri

### Adım Adım Kullanım

#### 1. Parametreleri Girin

**Temel Parametreler:**
- **Analiz Durumu**: Hangi senaryo (örn: "1")
- **Tasarım Numaraları**: Hangi tasarımlar (örn: "1,2,3")
- **Mod Sayısı**: Kaç mod hesaplanacak (örn: 8)
- **RNG Seed**: Rastgelelik kontrolü (örn: 12345)
- **Paralel İşlem**: Kaç çekirdek kullanılacak (örn: 4)

**Gelişmiş Ayarlar:**
- **Hesaplama Ortamı**: Local, HPC vb.
- **Batch/Job Ayarları**: HPC için

#### 2. Analizi Çalıştırın

- "▶️ Ön Analizi Çalıştır" butonuna tıklayın
- Ekranda örnek Python kodu görünecek
- Bu kodu kendi projenize kopyalayıp çalıştırın

#### 3. Sonuçları Görüntüleyin

- **Sonuç Dizini** kutusuna sonuç konumunu girin
- "📂 Sonuçları Yükle" butonuna tıklayın
- Bulunan dosyalardan birini seçin
- "📊 Görüntüle" ile sonuçları inceleyin
- "📥 CSV İndir" ile sonuçları kaydedin

### Örnek Çalışma

```
Analiz Durumu: 1
Tasarım Numaraları: 1,2
Mod Sayısı: 8
RNG Seed: 12345
Paralel İşlem: 4

Sonuç Dizini: /home/user/pypbee_work/Work_Dir/Prelim_Analysis_Results
```

---

## PSHA Analizi

### Ne İşe Yarar?

PSHA (Probabilistic Seismic Hazard Analysis), belirli bir konumda deprem tehlikesini olasılıksal olarak değerlendirir.

**Çıktılar:**
- Sismik tehlike eğrileri
- Deagregasyon grafikleri
- Tekdüze tehlike spektrumları (UHS)

### Adım Adım Kullanım

#### 1. Parametreleri Girin

**Sol Panel:**
- Analiz durumu
- Tasarım numaraları
- Paralel işlem sayısı

**IM Input Değerleri:**
```
0.1
0.2
0.3
0.5
0.7
1.0
```
Her satıra bir Intensity Measure değeri girin.

#### 2. Gelişmiş Ayarlar

- Hesaplama ortamı seçin
- HPC ayarları (gerekirse)

#### 3. Sonuçları Analiz Edin

**Tehlike Eğrisi Çizme:**
1. "📂 Sonuçları Yükle" tıklayın
2. "📊 Tehlike Eğrisi Çiz" ile grafik oluşturun
3. "📥 Grafik İndir" ile PNG kaydedin

**Detaylı İnceleme:**
1. Sonuç dosyası seçin
2. "🔍 Detayları Görüntüle" tıklayın
3. Veri tablosunu inceleyin
4. "📥 Tüm Sonuçları CSV İndir" ile kaydedin

### Yorumlama

**Tehlike Eğrisi Nasıl Okunur:**
- X ekseni: Intensity Measure (IM)
- Y ekseni: Yıllık aşılma olasılığı
- Eğrinin sola kayması: Yüksek tehlike
- Eğrinin sağa kayması: Düşük tehlike

---

## GMS - Yer Hareketi Seçimi

### Ne İşe Yarar?

GMS, hedef spektruma en uygun yer hareketi kayıtlarını seçer ve ölçeklendirir.

**Önemli Kavramlar:**
- **Hedef Spektrum**: Eşleştirilecek spektrum
- **Ölçeklendirme Faktörü**: Kayıtların çarpanı
- **Pulse-like**: Yakın fay etkisi

### Adım Adım Kullanım

#### 1. Tehlike Seviyelerini Tanımlayın

**Üç parametre seti girin:**
```
Tehlike Seviyeleri:  1,2,3
MRP (yıl):          72,475,2475
Kayıt Sayıları:     11,11,11
```

Her tehlike seviyesi için:
- Ortalama dönüş periyodu (MRP)
- Kaç kayıt seçileceği

#### 2. Seçim Parametreleri

**Ölçeklendirme Limitleri:**
- **Max Ölçek**: En fazla kaç kat büyütülebilir (örn: 4.0)
- **Min Ölçek**: En az kaç kat küçültülebilir (örn: 0.33)

**Seçim Ayarları:**
- ☑️ **UHS Kullan**: Tekdüze tehlike spektrumu
- ☑️ **Ölçeklendirilmiş**: Kayıtları ölçeklendir
- ☑️ **Pulse Sınıflandırma**: Yakın fay kayıtlarını ayırt et

#### 3. Sonuçları İnceleyin

**Spektral Eşleştirme Grafiği:**
- Kırmızı çizgi: Hedef spektrum
- Gri çizgiler: Seçilen kayıtlar
- Mavi kesikli: Ortalama spektrum

**Kayıt Listesi:**
- Seçilen her kayıt için:
  - Kayıt adı
  - Ölçeklendirme faktörü
  - MRP değeri
  - Tehlike seviyesi

### CSV Çıktısı

CSV dosyası şunları içerir:
- `analysis_key`: Analiz tanımlayıcısı
- `record`: Kayıt bilgisi
- `mrp`: Dönüş periyodu
- `n_gm`: Kayıt sayısı

---

## NLTHA Analizi

### Ne İşe Yarar?

NLTHA (Nonlinear Time-History Analysis), yapının seçilen yer hareketleri altında doğrusal olmayan davranışını analiz eder.

**Hesaplanan EDP'ler:**
- Kolon donatı birim şekil değiştirmesi
- Yay deformasyonları
- Çerçeve deplasmanları
- Özel tanımlı EDP'ler

### Adım Adım Kullanım

#### 1. EDP Türlerini Seçin

Hesaplanacak talep parametrelerini seçin:
- ☑️ MaxColRebarStrain (Kolon donatısı)
- ☑️ MaxSpringDeformation (Yay deformasyonu)
- ☑️ FrameMaxDeformation (Çerçeve deformasyonu)
- ☑️ Özel EDP (kendiniz tanımlayın)

#### 2. Analiz Ayarları

**Temel Ayarlar:**
- Analiz durumu
- Tasarım numaraları
- Tehlike seviyeleri
- Paralel işlem sayısı

**Staging Ayarları:**
- Staging pool size (hazırlık için)
- GM veritabanı dizini
- Arias Intensity sonlandırma

#### 3. Sonuç Görüntüleme

**Üç Görselleştirme Seçeneği:**

1. **Zaman Serisi:**
   - EDP'nin zamana göre değişimi
   - Maksimum/minimum noktalar
   - Kalıcı deformasyon

2. **EDP Dağılımı:**
   - Histogram
   - İstatistiksel özetler
   - Medyan, ortalama, std sapma

3. **Dosya İçeriği:**
   - Ham veri
   - Tablo formatında
   - İstatistikler

### Sonuç Yorumlama

**Zaman Serisi Grafiği:**
- İlk büyük tepeler: P-dalgası gelişi
- En büyük tepeler: S-dalgası
- Sönümleme: Yapısal sönüm

**Dağılım Grafiği:**
- Sağa çarpık dağılım: Lognormal EDP
- Medyan değer: Tasarım için önemli
- Aşırı değerler: Kapanma limitleri

---

## PSDemHA - Talep Tehlike Analizi

### Ne İşe Yarar?

PSDemHA, yapısal talep parametrelerinin (EDP) tehlike eğrilerini hesaplar.

**Önemli Çıktı:**
- EDP-Tehlike ilişkisi
- Belirli EDP değerinin aşılma olasılığı
- Çoklu EDP için karşılaştırma

### Adım Adım Kullanım

#### 1. EDP Listesini Tanımlayın

**EDP Tag'leri girin:**
```
1,2,3
```
Her tag bir EDP'yi temsil eder (örn: 1=kolon, 2=yay, 3=deplasman)

#### 2. Tehlike Parametreleri

**Delta Input:**
Her EDP için integrasyon adımı:
```
0.001
0.001
0.01
```

**Ölçek Faktörleri:**
- Minimum: Küçültme limiti (örn: 1.0)
- Maksimum: Büyütme limiti (örn: 1.0)

#### 3. Talep Tehlike Eğrisi

**Grafik Yorumlama:**
- X ekseni: EDP değeri
- Y ekseni: Yıllık aşılma olasılığı
- Kırmızı noktalar: Hedef performans noktaları

**Önemli Noktalar:**
- **2% / 50 yıl**: Tasarım depremi
- **10% / 50 yıl**: Servis depremi
- **50% / 50 yıl**: Sık deprem

### Performans Değerlendirmesi

```
EDP Değeri | Yıllık Aşılma | Yorumlama
-----------|---------------|------------------
0.001      | 0.02         | Yüksek performans
0.005      | 0.10         | Can güvenliği
0.010      | 0.50         | Sınır durum
```

---

## PSDamHA - Hasar Tehlike Analizi

### Ne İşe Yarar?

PSDamHA, hasar durumlarının tehlike eğrilerini ve kırılganlık fonksiyonlarını hesaplar.

**Hasar Durumları:**
1. **Hafif Hasar**: Kozmetik onarım
2. **Orta Hasar**: Yapısal onarım
3. **Şiddetli Hasar**: Güçlendirme gerekli
4. **Göçme**: Yıkım

### Adım Adım Kullanım

#### 1. Hasar Durumu Parametreleri

**DS Tag'leri:**
```
1,2,3
```
Her tag bir hasar durumu

**Çözüm Tipi:**
- **Numerical**: Sayısal integrasyon (daha hassas)
- **Analytical**: Analitik çözüm (daha hızlı)

#### 2. Kırılganlık Parametreleri

**Her DS için tanımlanır:**
- Medyan değer (θ)
- Lognormal standart sapma (β)
- Örnekleme sayısı

#### 3. Grafik Çeşitleri

**A) Hasar Tehlike Eğrisi:**
- Her DS için ayrı eğri
- Renkler: Yeşil → Turuncu → Kırmızı
- Şiddet arttıkça sola kayar

**B) Kırılganlık Eğrileri:**
- Her DS için hasar olasılığı
- S-şekilli eğriler
- Medyan değerde %50 olasılık

### Örnek Yorumlama

**Kırılganlık Eğrisi:**
```
EDP = 0.005:
- Hafif Hasar: %80 olasılık
- Orta Hasar: %30 olasılık
- Şiddetli Hasar: %5 olasılık
```

**Yorumlama:**
EDP değeri 0.005 olduğunda:
- Muhtemelen hafif hasar görülür
- Orta hasar mümkün ama düşük olasılık
- Şiddetli hasar çok az olası

---

## Sonuç İndirme ve Export

### CSV İndirme

**Her analiz için:**
1. Sonuçları görüntüleyin
2. "📥 CSV İndir" butonuna tıklayın
3. Dosya otomatik indirilir

**CSV Formatı:**
- UTF-8 kodlama (Türkçe karakter desteği)
- Başlık satırı mevcut
- Virgülle ayrılmış değerler

### Grafik İndirme

**Tüm grafikler için:**
1. Grafiği oluşturun
2. "📥 Grafik İndir" butonuna tıklayın
3. PNG formatında kaydedilir

**Grafik Özellikleri:**
- **Çözünürlük**: 300 DPI (yayın kalitesi)
- **Format**: PNG (şeffaf arka plan)
- **Boyut**: Otomatik optimizasyon

### Toplu İndirme

**Tüm sonuçları indirmek için:**
```python
# Python scripti ile
import os
import shutil

source_dir = "/path/to/results"
target_dir = "/path/to/backup"

shutil.copytree(source_dir, target_dir)
```

---

## Sık Sorulan Sorular

### 1. Arayüz açılmıyor, ne yapmalıyım?

**Çözüm:**
```bash
# Port meşgul olabilir, farklı port deneyin:
streamlit run web_interface.py --server.port 8502
```

### 2. Grafikler görünmüyor?

**Çözüm:**
```bash
# Matplotlib backend sorunudur:
pip install --upgrade matplotlib
```

### 3. CSV dosyası Türkçe karakter sorunu?

**Çözüm:**
- Excel'de: "Veri → Dosyadan → Metin/CSV"
- Kodlama olarak UTF-8 seçin

### 4. Büyük sonuç dosyaları yüklenmiy or?

**Çözüm:**
```python
# Streamlit config ayarı:
# .streamlit/config.toml oluşturun:
[server]
maxUploadSize = 1000
```

### 5. Python kodu hata veriyor?

**Kontrol listesi:**
- ✅ PyPBEE doğru kurulmuş mu?
- ✅ Model dosyaları mevcut mu?
- ✅ OpenSees kurulu mu?
- ✅ Gerekli tüm paketler yüklü mü?

### 6. Sonuçlar nerede saklanıyor?

**Varsayılan konum:**
```
~/pypbee_work/Work_Dir/
├── Prelim_Analysis_Results/
├── PSHA_Results/
├── GMS_Results/
├── NLTHA_Results/
├── PSDemHA_Results/
└── PSDamHA_Results/
```

### 7. Paralel işlem sayısını nasıl seçmeliyim?

**Öneriler:**
- Laptop: 2-4 çekirdek
- Masaüstü: 4-8 çekirdek
- Sunucu: CPU'ya göre (max %80)

**Kontrol:**
```python
import os
print(os.cpu_count())  # Toplam çekirdek
```

### 8. OpenSees modeli nasıl hazırlarım?

**Gereken dosyalar:**
- Model tanım dosyası (.tcl veya .py)
- Ön analiz scripti
- Recorder tanımları
- NLTHA çalıştırıcı

**Örnek yapı:**
```
model_files/
├── osb_info.py          # Model parametreleri
├── ops_model.py         # OpenSees modeli
└── run_prelim.tcl       # Ön analiz scripti
```

---

## Sorun Giderme

### Hata: "ModuleNotFoundError"

```bash
# Çözüm:
pip install -r requirements.txt
```

### Hata: "FileNotFoundError"

**Kontrol edin:**
1. Dosya yolu doğru mu?
2. Dosya gerçekten var mı?
3. Yazma/okuma izni var mı?

```bash
# İzinleri kontrol et:
ls -la /path/to/file

# İzin ver:
chmod 644 /path/to/file
```

### Hata: "PermissionError"

```bash
# Linux/Mac:
sudo chown -R $USER:$USER /path/to/work_dir

# Windows:
# Dosya → Özellikler → Güvenlik → Tam Denetim
```

### Streamlit Donuyor

**Çözümler:**
1. Tarayıcı cache temizle (Ctrl+Shift+Delete)
2. Farklı tarayıcı dene (Chrome, Firefox)
3. Streamlit'i yeniden başlat (Ctrl+C → yeniden çalıştır)

### Grafik Çizilmiyor

**Matplotlib sorunu:**
```bash
pip uninstall matplotlib
pip install matplotlib==3.8.2
```

### Bellek Hatası

**Büyük veri setleri için:**
```python
# Veriyi parça parça yükle:
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```

---

## Ek Kaynaklar

### Öğretici Videolar
(Gelecekte eklenecek)

### Örnek Projeler
- `examples/Bridge_A/`: Basit köprü modeli
- `examples/Bridge_B/`: Gelişmiş köprü modeli
- `examples/Bridge_MAOC/`: Çok açıklıklı köprü

### Faydalı Linkler
- [PyPBEE GitHub](https://github.com/angshuman311/PyPBEE)
- [OpenSees Dokümantasyon](https://opensees.berkeley.edu/)
- [PEER NGA Database](https://ngawest2.berkeley.edu/)
- [Streamlit Dokümantasyon](https://docs.streamlit.io/)

### İletişim
- GitHub Issues: Hata bildirimi ve öneriler
- Discussions: Genel sorular ve tartışmalar

---

## Katkıda Bulunma

Bu dokümana katkı sağlamak isterseniz:
1. Eksik bulduğunuz bölümleri bildirin
2. Daha net açıklamalar önerin
3. Örnek ekran görüntüleri paylaşın
4. Yeni FAQ soruları ekleyin

**Teşekkürler ve başarılı analizler! 🎉**
