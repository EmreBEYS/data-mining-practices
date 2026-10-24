
# Mini Problem 08 — Normal KNN ve Ağırlıklı KNN ile Satın Alma Tahmini

Bir e-ticaret uygulamasında kullanıcının bir ürünü satın alıp almayacağını tahmin etmek istiyoruz.

Bu problemde **Normal KNN (K-Nearest Neighbors)** ve **Ağırlıklı KNN (Weighted KNN)** algoritmalarını karşılaştıracağız.

Amaç, en yakın komşulara eşit oy hakkı vermek ile uzaklıklarına göre ağırlık vermenin tahmin sonucunu nasıl değiştirdiğini incelemektir.

---

## 1. Veri Kümesi

Yeni kullanıcı ile en yakın üç müşterinin uzaklıkları şöyledir:

| Müşteri | Uzaklık | Satın aldı mı? |
|---------|:-------:|:--------------:|
| A | 1 | Evet |
| B | 2 | Hayır |
| C | 3 | Hayır |

Komşu sayısı:

$$
k=3
$$

**Soru:** Normal KNN ve Ağırlıklı KNN algoritmalarına göre yeni kullanıcının satın alma tahmini ne olur?

---

## 2. Normal KNN Nedir?

Normal KNN, yeni bir veri noktasının sınıfını belirlemek için en yakın k komşunun sınıflarını kullanır.

Sınıflandırma işleminde her komşunun oyu eşittir.

### Normal KNN Çalışma Mantığı

1. Yeni kullanıcıya en yakın k komşu belirlenir.
2. Komşuların sınıfları incelenir.
3. Her komşu bir oy kullanır.
4. En fazla oyu alan sınıf seçilir.

Bu problemde:

$$
k=3
$$

---

## 3. Normal KNN ile Elle Çözüm

### Adım 1 — Komşuların Belirlenmesi

| Müşteri | Uzaklık | Sınıf | Oy |
|---------|:-------:|:-----:|:--:|
| A | 1 | Evet | 1 |
| B | 2 | Hayır | 1 |
| C | 3 | Hayır | 1 |

### Adım 2 — Sınıf Oylarının Hesaplanması

Evet sınıfı:

$$
Evet=1
$$

Hayır sınıfı:

$$
Hayır=2
$$

### Adım 3 — Çoğunluk Oylaması

Sınıf oy oranları:

$$
P(Evet)=\frac{1}{3}\approx0{,}3333
$$

$$
P(Hayır)=\frac{2}{3}\approx0{,}6667
$$

Hayır sınıfı daha fazla oy aldığı için:

$$
\boxed{\text{Normal KNN}=\text{HAYIR}}
$$

**Yorum:** Normal KNN algoritması, B ve C müşterilerinin oylarını eşit ağırlıkla değerlendirdiği için yeni kullanıcının ürünü satın almayacağını tahmin eder.

---

## 4. Ağırlıklı KNN Nedir?

Ağırlıklı KNN, normal KNN'den farklı olarak her komşunun oyuna uzaklığına bağlı bir ağırlık verir.

Yakın komşular daha yüksek, uzak komşular daha düşük ağırlığa sahip olur.

Bu problemde uzaklığın karesiyle ters orantılı ağırlık kullanacağız.

### Ağırlık Formülü

$$
w_i=\frac{1}{d_i^2}
$$

Burada:

- $w_i$: i. komşunun ağırlığı
- $d_i$: i. komşunun yeni kullanıcıya uzaklığı

**Önemli:** Bu formül, uzaklık sıfırdan büyük olduğunda doğrudan uygulanır. Uzaklığı sıfır olan komşular için özel işlem gerekir.

---

## 5. Ağırlıklı KNN ile Elle Çözüm

### Adım 1 — A Müşterisinin Ağırlığı

A müşterisinin uzaklığı:

$$
d_A=1
$$

Ağırlık hesabı:

$$
w_A=\frac{1}{1^2}
$$

$$
\boxed{w_A=1}
$$

A müşterisinin sınıfı **Evet** olduğundan bu ağırlık Evet sınıfına eklenir.

---

### Adım 2 — B Müşterisinin Ağırlığı

B müşterisinin uzaklığı:

$$
d_B=2
$$

Ağırlık hesabı:

$$
w_B=\frac{1}{2^2}
$$

$$
w_B=\frac{1}{4}
$$

$$
\boxed{w_B=0{,}25}
$$

B müşterisinin sınıfı **Hayır** olduğundan bu ağırlık Hayır sınıfına eklenir.

---

### Adım 3 — C Müşterisinin Ağırlığı

C müşterisinin uzaklığı:

$$
d_C=3
$$

Ağırlık hesabı:

$$
w_C=\frac{1}{3^2}
$$

$$
w_C=\frac{1}{9}
$$

$$
\boxed{w_C\approx0{,}1111}
$$

C müşterisinin sınıfı **Hayır** olduğundan bu ağırlık Hayır sınıfına eklenir.

---

## 6. Sınıf Ağırlıklarının Hesaplanması

Her sınıfın toplam ağırlığı hesaplanır.

### Evet Sınıfı

Evet sınıfında yalnızca A müşterisi bulunmaktadır.

$$
W(Evet)=w_A
$$

$$
\boxed{W(Evet)=1}
$$

### Hayır Sınıfı

Hayır sınıfında B ve C müşterileri bulunmaktadır.

$$
W(Hayır)=w_B+w_C
$$

$$
=\frac{1}{4}+\frac{1}{9}
$$

$$
=0{,}25+0{,}1111
$$

$$
\boxed{W(Hayır)\approx0{,}3611}
$$

---

## 7. Ağırlıklı KNN Kararı

Toplam ağırlıklar:

$$
W(Evet)=1
$$

$$
W(Hayır)\approx0{,}3611
$$

Karşılaştırma:

$$
W(Evet)>W(Hayır)
$$

Bu nedenle:

$$
\boxed{\text{Ağırlıklı KNN}=\text{EVET}}
$$

**Yorum:** A müşterisi diğerlerinden çok daha yakın olduğu için ağırlığı daha yüksektir. Böylece tek bir Evet oyu, iki Hayır oyunun toplam ağırlığından büyük olmuştur.

---

## 8. Normal KNN ve Ağırlıklı KNN Karşılaştırması

| Özellik | Normal KNN | Ağırlıklı KNN |
|---------|------------|---------------|
| Komşu sayısı | 3 | 3 |
| Komşular | A, B, C | A, B, C |
| Oy yaklaşımı | Eşit oy | Uzaklığa bağlı ağırlık |
| Evet skoru | 1 | 1,0000 |
| Hayır skoru | 2 | 0,3611 |
| **Tahmin** | **HAYIR** | **EVET** |

### Sonuçların Farklı Olmasının Nedeni

Normal KNN algoritmasında:

$$
1<2
$$

Bu nedenle Hayır sınıfı seçilir.

Ağırlıklı KNN algoritmasında:

$$
1>0{,}3611
$$

Bu nedenle Evet sınıfı seçilir.

Yani yakın komşulara daha fazla önem verilmesi, sınıflandırma sonucunu değiştirmiştir.

---

## 9. Normalize Edilmiş Ağırlıklar

Ağırlıklı KNN sonuçlarını daha kolay yorumlayabilmek için sınıf ağırlıklarını normalize edebiliriz.

Toplam ağırlık:

$$
W_{toplam}=1+\frac{1}{4}+\frac{1}{9}
$$

$$
W_{toplam}=\frac{49}{36}\approx1{,}3611
$$

Evet sınıfının ağırlık oranı:

$$
P_w(Evet)=\frac{1}{49/36}
$$

$$
\boxed{P_w(Evet)\approx0{,}7347}
$$

Hayır sınıfının ağırlık oranı:

$$
P_w(Hayır)=\frac{13/36}{49/36}
$$

$$
\boxed{P_w(Hayır)\approx0{,}2653}
$$

Bu oranlar:

- Evet: %73,47
- Hayır: %26,53

**Not:** Bu değerler normalize edilmiş komşu ağırlıklarıdır; doğrudan kalibre edilmiş satın alma olasılığı olarak değerlendirilmemelidir.

---

## 10. Genel Değerlendirme

Bu problemde iki farklı KNN yaklaşımı kullanılarak aynı kullanıcı için satın alma tahmini gerçekleştirilmiştir.

Normal KNN, her komşuya eşit oy hakkı verdiği için **HAYIR** sonucunu üretmiştir.

Ağırlıklı KNN ise en yakın komşuya daha fazla önem verdiği için **EVET** sonucunu üretmiştir.

### Önemli Çıkarımlar

- Komşuların uzaklıkları sınıflandırma sonucunu etkileyebilir.
- Normal KNN tüm komşuları eşit değerlendirir.
- Ağırlıklı KNN yakın komşuların etkisini artırır.
- Ağırlıklandırma yöntemi değiştiğinde tahmin sonucu da değişebilir.
- Her problemde ağırlıklı KNN'nin daha başarılı olacağı garanti değildir.
- En uygun yöntem doğrulama verileriyle karşılaştırılarak seçilmelidir.

### Nihai Sonuç

$$
\boxed{\text{Normal KNN}=\text{HAYIR}}
$$

$$
\boxed{\text{Ağırlıklı KNN}=\text{EVET}}
$$

**Bu örnek, komşuların yalnızca sayısının değil, uzaklıklarının da sınıflandırma kararını değiştirebildiğini göstermektedir.**
