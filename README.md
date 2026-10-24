# Veri Madenciliği Ders Uygulamaları

Bu depo, **Veri Madenciliği** dersi kapsamında işlenen temel algoritmaların, matematiksel yöntemlerin ve makine öğrenmesi tekniklerinin hem teorik hem de uygulamalı biçimde incelenmesi amacıyla hazırlanmıştır.

Çalışmalar; elle çözülen sayısal problemleri, Python uygulamalarını, algoritma karşılaştırmalarını ve elde edilen sonuçların değerlendirilmesini içermektedir.

## İçerik

### 1. Python Uygulamaları

| No | Uygulama | Öğrenme Amacı |
|---:|---|---|
| 01 | [Entropi ve Bilgi Kazancı](uygulamalar/01_entropi_bilgi_kazanci/README.md) | Entropi ve bilgi kazancını sıfırdan hesaplamak |
| 02 | [Kredi Riski Karar Ağacı](uygulamalar/02_kredi_riski_karar_agaci/README.md) | Kategorik ve sayısal verilerle karar ağacı oluşturmak |
| 03 | [Iris Eğitim-Test ve Confusion Matrix](uygulamalar/03_iris_egitim_test_confusion_matrix/README.md) | Model eğitimi, sınıflandırma ve hata matrisi oluşturmak |
| 04 | [Sayısal Örnek Doğrulama](uygulamalar/04_sayisal_ornek_dogrulama/README.md) | Elle hesaplanan entropi, bilgi kazancı ve Gini değerlerini Python ile doğrulamak |

### 2. Mini Problemler — Elle Çözüm

Bu bölümde algoritmaların matematiksel temelleri küçük veri kümeleri üzerinde adım adım incelenmektedir.

| No | Mini Problem | Kullanılan Yöntem | Sonuç |
|---:|---|---|---|
| 01 | [Gini ile Sınav Başarısı](mini_problemler/01_gini/README.md) | Gini İndeksi | Ağırlıklı Gini = 0,375 |
| 02 | [Twoing ile İş Memnuniyeti](mini_problemler/02_twoing/README.md) | Twoing Kriteri | Twoing = 0,64 |
| 03 | [KNN ile Öğrenci Başarı Tahmini](mini_problemler/03_knn/README.md) | KNN, Öklid Uzaklığı | GEÇTİ |
| 04 | [Normal KNN ve Ağırlıklı KNN](mini_problemler/04_weighted_knn/README.md) | KNN, Weighted KNN | HAYIR / EVET |

*Not: Twoing sonucu, ders örneğinde kullanılan formül tanımına göredir.*

## Kullanılan Algoritmalar

### Karar Ağacı Algoritmaları

**Entropi**

Bir veri kümesindeki belirsizliği ölçer.

$$
H(S)=-\sum_{i=1}^{k}p_i\log_2(p_i)
$$

**Bilgi Kazancı**

Bir özelliğe göre bölünmenin belirsizliği ne kadar azalttığını ölçer.

$$
IG(S,A)=H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v)
$$

**Gini İndeksi**

Bir veri kümesinin sınıfsal safsızlığını hesaplar.

$$
Gini(S)=1-\sum_{i=1}^{k}p_i^2
$$

**Twoing Kriteri**

İki alt grubun sınıf dağılımlarındaki farklılığı değerlendirir.

Ders örneklerinde kullanılan biçimi:

$$
\Phi=2P_LP_R\sum_j|P(j|L)-P(j|R)|
$$

### K-En Yakın Komşu (KNN)

KNN, yeni bir örneği en yakın komşularının sınıflarına göre sınıflandırır.

**Öklid Uzaklığı**

$$
d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

**Ağırlıklı KNN**

Yakın komşulara daha fazla önem vermek için uzaklığın karesiyle ters orantılı ağırlık kullanılabilir.

$$
w_i=\frac{1}{d_i^2}
$$

Bu formül pozitif uzaklıklar için geçerlidir. Sıfır uzaklık durumları ayrıca ele alınmalıdır.

## Kurulum

Python 3.10 veya üzeri önerilir.

Depoyu bilgisayarınıza aldıktan sonra ana dizinde sanal ortam oluşturun:

```bash
python -m venv .venv
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**macOS / Linux**

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Python Uygulamalarını Çalıştırma

Komutları depo ana dizininde çalıştırın.

```bash
python uygulamalar/01_entropi_bilgi_kazanci/app.py
python uygulamalar/02_kredi_riski_karar_agaci/app.py
python uygulamalar/03_iris_egitim_test_confusion_matrix/app.py
python uygulamalar/04_sayisal_ornek_dogrulama/app.py
```

Programlar varsayılan olarak sonuçlarını kendi `sonuclar/` klasörlerine kaydeder.

Özel bir çıktı klasörü seçmek için:

```bash
python uygulamalar/03_iris_egitim_test_confusion_matrix/app.py --output-dir kendi_sonuclarim
```

## Testler

Otomatik testleri çalıştırmak için:

```bash
python -m pytest -q
```

Testler matematiksel hesaplamaların doğruluğunu, model çıktılarının oluşturulmasını ve uygulamaların beklenen sonuçlarını kontrol etmek amacıyla hazırlanmıştır.

## Öğrenme Hedefleri

Bu depo kapsamında aşağıdaki konuların öğrenilmesi hedeflenmektedir:

- Entropi ve bilgi kazancı hesaplamaları
- Karar ağaçlarının çalışma mantığı
- Gini ve Twoing bölünme kriterleri
- KNN algoritması ve Öklid uzaklığı
- Normal KNN ve Ağırlıklı KNN karşılaştırması
- Eğitim ve test kümelerinin ayrılması
- Confusion Matrix ile model değerlendirme
- Matematiksel hesaplamaların Python ile doğrulanması
- Algoritmaların avantaj ve dezavantajlarının incelenmesi

## Proje Yapısı

```text
Veri-Madenciligi/
│
├── README.md
├── requirements.txt
│
├── uygulamalar/
│   ├── 01_entropi_bilgi_kazanci/
│   ├── 02_kredi_riski_karar_agaci/
│   ├── 03_iris_egitim_test_confusion_matrix/
│   └── 04_sayisal_ornek_dogrulama/
│
├── mini_problemler/
│   ├── 01_gini/
│   │   └── README.md
│   ├── 02_twoing/
│   │   └── README.md
│   ├── 03_knn/
│   │   └── README.md
│   └── 04_weighted_knn/
│       └── README.md
│
└── tests/
```

*Proje ağacındaki mini problem klasörleri önerilen düzeni göstermektedir.*

## Akademik Not

Bu depoda kullanılan küçük veri kümeleri eğitim ve algoritma analizi amacıyla hazırlanmıştır.

Örneklerde elde edilen sonuçlar gerçek dünyadaki başarı, finansal risk veya satın alma davranışları için doğrudan güvenilir tahminler olarak değerlendirilmemelidir.

Algoritmaların gerçek veri kümelerinde kullanılabilmesi için uygun veri ön işleme, model değerlendirme ve doğrulama süreçleri uygulanmalıdır.

---

**Veri Madenciliği Ders Uygulamaları — Teoriden Python Uygulamasına**