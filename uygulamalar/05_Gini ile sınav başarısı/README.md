
# Mini Problem 05 — Gini ile Sınav Başarısı

Bir öğretmenin **8 öğrencisi** bulunuyor. Öğretmen, öğrencilerin çalışma durumlarına göre sınavı geçip geçmediklerini tahmin etmek istiyor.

Bu problemde **Gini İndeksi** kullanılarak çalışma durumuna göre veri kümesinin safsızlığı hesaplanacaktır.

## 1. Veri Kümesi

| Çalışma Durumu | Geçti | Kaldı | Toplam |
|----------------|:-----:|:-----:|:------:|
| Düzenli        | 3     | 1     | 4      |
| Düzensiz       | 1     | 3     | 4      |
| **Toplam**     | **4** | **4** | **8**  |

## 2. Gini İndeksi Nedir?

Gini İndeksi, karar ağaçlarında bir veri kümesinin ne kadar saf veya karışık olduğunu ölçmek için kullanılır.

Genel formül:

$$
Gini(D)=1-\sum_{i=1}^{k}p_i^2
$$

Burada:

- $D$: Veri kümesi
- $k$: Sınıf sayısı
- $p_i$: İlgili sınıfın veri kümesindeki oranı

**Yorum:**

- Gini = 0 → Tamamen saf veri kümesi.
- Gini değeri arttıkça sınıfların karışıklığı artar.
- İki sınıflı bir problemde maksimum Gini değeri 0,5'tir.

---

## 3. Elle Çözüm

### Adım 1 — Düzenli Çalışanlar

Düzenli çalışan toplam 4 öğrenci vardır.

- Sınavı geçen: 3
- Sınavda kalan: 1

Sınıf olasılıkları:

$$
P(Geçti)=\frac{3}{4}
$$

$$
P(Kaldı)=\frac{1}{4}
$$

Gini hesabı:

$$
Gini_D=1-\left(\frac{3}{4}\right)^2-\left(\frac{1}{4}\right)^2
$$

$$
=1-\frac{9}{16}-\frac{1}{16}
$$

$$
=1-\frac{10}{16}
$$

$$
\boxed{Gini_D=0{,}375}
$$

### Adım 2 — Düzensiz Çalışanlar

Düzensiz çalışan toplam 4 öğrenci vardır.

- Sınavı geçen: 1
- Sınavda kalan: 3

Sınıf olasılıkları:

$$
P(Geçti)=\frac{1}{4}
$$

$$
P(Kaldı)=\frac{3}{4}
$$

Gini hesabı:

$$
Gini_R=1-\left(\frac{1}{4}\right)^2-\left(\frac{3}{4}\right)^2
$$

$$
=1-\frac{1}{16}-\frac{9}{16}
$$

$$
=1-\frac{10}{16}
$$

$$
\boxed{Gini_R=0{,}375}
$$

---

## 4. Ağırlıklı Gini Hesabı

Karar ağacında bölünme sonrası toplam safsızlık, alt grupların büyüklükleri dikkate alınarak hesaplanır.

Genel formül:

$$
Gini_{split}=\sum_{j=1}^{m}\frac{|D_j|}{|D|}Gini(D_j)
$$

Bu problemde:

- Toplam öğrenci sayısı: 8
- Düzenli çalışan: 4
- Düzensiz çalışan: 4

$$
Gini_B=\frac{4}{8}(0{,}375)+\frac{4}{8}(0{,}375)
$$

$$
=0{,}1875+0{,}1875
$$

$$
\boxed{Gini_B=0{,}375}
$$

---

## 5. Başlangıç Gini Değeri

Bölünmeden önce veri kümesinde:

- Geçen öğrenci: 4
- Kalan öğrenci: 4

$$
Gini_{ilk}=1-\left(\frac{4}{8}\right)^2-\left(\frac{4}{8}\right)^2
$$

$$
=1-0{,}25-0{,}25
$$

$$
\boxed{Gini_{ilk}=0{,}5}
$$

## 6. Gini Azalışı

$$
\Delta Gini=Gini_{ilk}-Gini_B
$$

$$
=0{,}5-0{,}375
$$

$$
\boxed{\Delta Gini=0{,}125}
$$

Çalışma durumuna göre bölünme, veri kümesinin safsızlığını **0,125 azaltmıştır**.

---

## 7. Sonuçların Değerlendirilmesi

| Ölçüt | Gini Değeri |
|-------|:-----------:|
| Başlangıç Gini | 0,500 |
| Düzenli çalışanlar | 0,375 |
| Düzensiz çalışanlar | 0,375 |
| Ağırlıklı Gini | 0,375 |
| Gini azalışı | 0,125 |

**Sonuç:**

Bu veri kümesinde çalışma durumuna göre bölünmenin safsızlığı **0,375** olarak hesaplanmıştır.

Düzenli çalışan öğrencilerin %75'i sınavı geçerken düzensiz çalışan öğrencilerin %25'i sınavı geçmiştir.

Bu nedenle çalışma durumu, sınav başarısını tahmin etmede faydalı bir özellik olabilir.

Ancak Gini değeri sıfır olmadığı için oluşturulan alt gruplar tamamen saf değildir.

Başka özellikler bulunuyorsa onların da Gini değerleri hesaplanarak en iyi bölünme seçilebilir.
