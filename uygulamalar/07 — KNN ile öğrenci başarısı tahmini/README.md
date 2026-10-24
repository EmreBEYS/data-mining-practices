
# Mini Problem 07 — KNN ile Öğrenci Başarı Tahmini

Bir öğrencinin haftalık çalışma saati ve çözdüğü deneme sayısını kullanarak sınav başarısını tahmin edeceğiz.

Bu problemde **K-En Yakın Komşu (K-Nearest Neighbors / KNN)** algoritması kullanılarak yeni bir öğrencinin sınavı geçip geçmeyeceği belirlenecektir.

## 1. Veri Kümesi

İki özellik kullanılmıştır:

- **X₁:** Haftalık çalışma saati
- **X₂:** Çözülen deneme sayısı

| Öğrenci | X₁ | X₂ | Başarı |
|---------|:--:|:--:|:------:|
| A | 1 | 2 | Kaldı |
| B | 2 | 3 | Kaldı |
| C | 4 | 4 | Geçti |
| D | 5 | 5 | Geçti |
| E | 6 | 4 | Geçti |

### Yeni Öğrenci

Yeni öğrencinin özellikleri:

$$
P=(3,4)
$$

Komşu sayısı:

$$
k=3
$$

**Soru:** Bu öğrencinin başarı sınıfı ne olur?

---

## 2. KNN Algoritması Nedir?

KNN, makine öğrenmesinde kullanılan gözetimli bir öğrenme algoritmasıdır.

Yeni bir veri noktasının sınıfını, eğitim kümesindeki en yakın k komşusunun sınıflarına bakarak belirler.

### KNN Çalışma Mantığı

1. Yeni veri noktası belirlenir.
2. Diğer veri noktalarına olan uzaklıklar hesaplanır.
3. Uzaklıklar küçükten büyüğe sıralanır.
4. En yakın k komşu seçilir.
5. Sınıflandırmada çoğunluk oylaması uygulanır.
6. Yeni veri noktasının sınıfı tahmin edilir.

---

## 3. Öklid Uzaklığı

İki nokta arasındaki doğrusal uzaklığı hesaplamak için Öklid uzaklığı kullanılır.

İki boyutlu genel formül:

$$
d(A,B)=\sqrt{(x_{A1}-x_{B1})^2+(x_{A2}-x_{B2})^2}
$$

Yeni öğrencimiz:

$$
P=(3,4)
$$

Bu nedenle uzaklık formülümüz:

$$
d=\sqrt{(x_1-3)^2+(x_2-4)^2}
$$

---

## 4. Elle Çözüm

### Adım 1 — A Öğrencisinin Uzaklığı

A öğrencisinin özellikleri:

$$
A=(1,2)
$$

Öklid uzaklığı:

$$
d_A=\sqrt{(1-3)^2+(2-4)^2}
$$

$$
=\sqrt{(-2)^2+(-2)^2}
$$

$$
=\sqrt{4+4}
$$

$$
\boxed{d_A=\sqrt{8}\approx2{,}83}
$$

### Adım 2 — B Öğrencisinin Uzaklığı

B öğrencisinin özellikleri:

$$
B=(2,3)
$$

$$
d_B=\sqrt{(2-3)^2+(3-4)^2}
$$

$$
=\sqrt{(-1)^2+(-1)^2}
$$

$$
=\sqrt{1+1}
$$

$$
\boxed{d_B=\sqrt{2}\approx1{,}41}
$$

### Adım 3 — C Öğrencisinin Uzaklığı

C öğrencisinin özellikleri:

$$
C=(4,4)
$$

$$
d_C=\sqrt{(4-3)^2+(4-4)^2}
$$

$$
=\sqrt{1^2+0^2}
$$

$$
\boxed{d_C=1{,}00}
$$

### Adım 4 — D Öğrencisinin Uzaklığı

D öğrencisinin özellikleri:

$$
D=(5,5)
$$

$$
d_D=\sqrt{(5-3)^2+(5-4)^2}
$$

$$
=\sqrt{2^2+1^2}
$$

$$
=\sqrt{4+1}
$$

$$
\boxed{d_D=\sqrt{5}\approx2{,}24}
$$

### Adım 5 — E Öğrencisinin Uzaklığı

E öğrencisinin özellikleri:

$$
E=(6,4)
$$

$$
d_E=\sqrt{(6-3)^2+(4-4)^2}
$$

$$
=\sqrt{3^2+0^2}
$$

$$
\boxed{d_E=3{,}00}
$$

---

## 5. Uzaklıkların Sıralanması

Bütün öğrencilerin yeni öğrenciye olan uzaklıklarını küçükten büyüğe sıralayalım.

| Sıra | Öğrenci | Uzaklık | Sınıf |
|:----:|:-------:|:-------:|:-----:|
| 1 | C | 1,00 | Geçti |
| 2 | B | 1,41 | Kaldı |
| 3 | D | 2,24 | Geçti |
| 4 | A | 2,83 | Kaldı |
| 5 | E | 3,00 | Geçti |

En yakın üç komşu:

$$
k=3
$$

Seçilen öğrenciler:

- C → Geçti
- B → Kaldı
- D → Geçti

---

## 6. Çoğunluk Oylaması

KNN algoritmasında sınıflandırma için en yakın komşuların sınıfları değerlendirilir.

Seçilen 3 komşunun sınıf dağılımı:

$$
Geçti=2
$$

$$
Kaldı=1
$$

Sınıfların komşular arasındaki oranları:

$$
P(Geçti)=\frac{2}{3}\approx0{,}667
$$

$$
P(Kaldı)=\frac{1}{3}\approx0{,}333
$$

Çoğunluk oylaması sonucunda:

$$
\boxed{\text{Tahmin}=\text{GEÇTİ}}
$$

Bu nedenle yeni öğrencinin sınavı geçeceği tahmin edilmektedir.

---

## 7. Sonuçların Değerlendirilmesi

| Ölçüt | Sonuç |
|-------|:-----:|
| Yeni öğrenci | (3,4) |
| Komşu sayısı (k) | 3 |
| Uzaklık yöntemi | Öklid |
| En yakın komşu | C |
| En yakın 3 komşu | C, B, D |
| Geçti oyu | 2 |
| Kaldı oyu | 1 |
| **Tahmin edilen sınıf** | **GEÇTİ** |

### Sonuç

Yeni öğrencinin haftalık çalışma saati 3, çözdüğü deneme sayısı 4'tür.

KNN algoritması kullanılarak eğitim veri kümesindeki diğer öğrencilere olan uzaklıklar hesaplanmıştır.

En yakın üç komşudan ikisi sınavı geçtiği için yeni öğrenci **GEÇTİ** olarak sınıflandırılmıştır.

**Not:** %66,7 değeri üç komşu arasındaki oy oranıdır; modelin gerçek doğruluk oranını veya kalibre edilmiş başarı olasılığını göstermez.

---

## 8. KNN Algoritmasının Avantajları ve Dezavantajları

### Avantajları

- Öğrenmesi ve uygulanması kolaydır.
- Küçük veri kümelerinde etkili olabilir.
- Sınıflandırma ve regresyon problemlerinde kullanılabilir.
- Karmaşık bir model eğitimi gerektirmez.

### Dezavantajları

- Büyük veri kümelerinde tahmin maliyeti artabilir.
- Özelliklerin ölçeklerinden etkilenir.
- Gereksiz veya ilgisiz özelliklere duyarlıdır.
- K değerinin yanlış seçilmesi tahminleri etkileyebilir.

---

## 9. Önemli Notlar

Bu problemde:

- k = 3 seçilmiştir.
- Öklid uzaklığı kullanılmıştır.
- Özellikler aynı ölçekte kabul edilmiştir.
- Her komşunun oyu eşit ağırlıktadır.

Gerçek veri kümelerinde özellik ölçekleri farklıysa StandardScaler veya MinMaxScaler gibi normalizasyon/ölçeklendirme yöntemleri uygulanabilir.

En uygun k değeri çapraz doğrulama gibi yöntemlerle belirlenebilir.
