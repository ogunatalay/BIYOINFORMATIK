# 🧬 DNA ve Protein Analizi – Biyoinformatik Projesi

Bu proje, FASTA formatında verilen DNA ve protein dizileri üzerinde temel biyoinformatik işlemler gerçekleştirmek için geliştirilmiştir. Biopython kütüphanesi kullanılarak yapılan analizler hem nükleotid hem de protein dizilerini kapsamaktadır.

## 🔬 İçerik

### ✅ 1. DNA Analizleri

#### A. Nükleotid Frekansı Hesaplama
- `N` harfi hariç tüm nükleotidlerin frekansı hesaplanır.

#### B. DNA → RNA Dönüşümü
- DNA dizileri transkribe edilerek RNA'ya çevrilir ve yeni bir `.fasta` dosyasına kaydedilir.

#### C. DNA → Protein Dönüşümü (Özel Kodon Tablosu ile)
- DNA dizileri özel olarak tanımlanmış bir genetik kod tablosu kullanılarak proteine çevrilir.
- Stop kodonları geldiğinde çeviri durur.

#### E. GC İçeriği Hesaplama
- Her dizinin GC içeriği yüzdesel olarak hesaplanır.

#### F. Global Hizalama (pairwise2.align.globalxx)
- DNA dizileri çiftler halinde hizalanır, tüm olası eşleşmeler gösterilir.

#### G. Lokal Hizalama (pairwise2.align.localxx)
- DNA dizileri yerel olarak hizalanır, benzer motiflerin lokal hizalaması yapılır.

#### H. PFM (Position Frequency Matrix) Hesaplama
- Diziler arasındaki her pozisyonda A, C, G, T sıklıkları hesaplanır.

#### İ. PPM (Position Probability Matrix) Hesaplama
- PFM’den pozisyon bazlı nükleotid olasılıkları hesaplanır.

#### J. PWM (Position Weight Matrix) Hesaplama
- PPM üzerinden bilgi içeriği bazlı log2 tabanında ağırlıklar hesaplanır.

---

### ✅ 2. Protein Analizleri

#### A. Motif Arama (Regex ile)
- Kullanıcı tanımlı regex motifi (örnek: `. {5}`) ile protein dizileri taranır ve eşleşmeler raporlanır.

#### B. Global Hizalama
- Protein dizileri çiftler halinde global olarak hizalanır (en uzun eşleşme için).

#### C. Lokal Hizalama
- Protein dizileri lokal olarak hizalanır, ortak motifler bulunur.

#### D. Özelleştirilmiş Skorlarla Global ve Lokal Hizalama
- Kullanıcı tarafından belirlenen:
  - Eşleşme puanı
  - Eşleşmeme cezası
  - Boşluk açma cezası
  - Boşluk uzatma cezası  
  parametrelerine göre hizalama yapılır (`globalms`, `localms`).

---

## 💡 Kullanılan Kütüphaneler

- `biopython`
- `collections`
- `math`
- `re`

Kurulum:

## 📁 Girdi Dosyaları

Aşağıdaki FASTA formatındaki dosyaların proje dizininde (aynı klasörde) bulunması gerekmektedir:

- `DNA.fasta`  
  → DNA dizilerini içeren FASTA dosyası

- `Protein.fasta` veya `Protein_Dosyası.fasta`  
  → Protein dizilerini içeren FASTA dosyası

---

## ⚙️ Nasıl Kullanılır?

- Tüm kodlar bir Jupyter Notebook veya Google Colab ortamında çalıştırılabilir.
- Hücreler sırayla çalıştırıldığında her analiz fonksiyonu bağımsız olarak test edilebilir.
- Gerekli kütüphaneler yüklendikten sonra (örn: Biopython), analiz adımları herhangi bir modifikasyon olmadan çalıştırılabilir.

```bash
pip install biopython

## 📌 Proje Sahibi
- 👨‍💻 İsim: Ogün Atalay

- 📅 Proje: Biyoinformatik Projesi – 2025


