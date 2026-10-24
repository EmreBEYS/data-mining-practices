
# Mini Problem 06 — Twoing ile İş Memnuniyeti

Bir şirkette çalışanların görevlerine göre iş memnuniyetini inceleyelim.

Bu problemde **Twoing kriteri** kullanılarak çalışanların görev niteliklerine göre bölünmesinin kalitesi hesaplanacaktır.

## 1. Veri Kümesi

| Görev | Evet | Hayır | Toplam |
|-------|:----:|:-----:|:------:|
| Yönetici | 4 | 0 | 4 |
| Uzman | 2 | 4 | 6 |
| **Toplam** | **6** | **4** | **10** |

**Soru:** Görev niteliğine göre bölünmenin Twoing değeri nedir?

---

## 2. Twoing Kriteri Nedir?

Twoing, karar ağaçlarında kullanılan bir bölünme kriteridir.

Özellikle **CART (Classification and Regression Trees)** algoritmasında, iki alt grup arasındaki sınıf dağılımlarının farklılığını değerlendirmek için kullanılabilir.

Twoing kriterinde amaç, sınıf dağılımları birbirinden farklı olan iki grup oluşturmaktır.

### Twoing Formülü

$$
\Phi=2P_LP_R\sum_{j=1}^{k}|P(j|L)-P(j|R)|
$$

Burada:

- $\Phi$: Twoing değeri
- $P_L$: Sol gruptaki gözlemlerin oranı
- $P_R$: Sağ gruptaki gözlemlerin oranı
- $P(j|L)$: Sol grupta j sınıfının olasılığı
- $P(j|R)$: Sağ grupta j sınıfının olasılığı
- $k$: Sınıf sayısı

**Yorum:**

- Twoing değeri 0 ise iki grubun sınıf dağılımları aynıdır.
- Twoing değeri büyüdükçe gruplar arasındaki ayrım güçlenir.
- Bu tanıma göre Twoing değeri 0 ile 1 arasındadır.

---

## 3. Elle Çözüm

### Adım 1 — Sol ve Sağ Grupların Belirlenmesi

Sol grup (L): Yöneticiler

Sağ grup (R): Uzmanlar

Toplam çalışan sayısı:

$$
N=4+6=10
$$

Sol grubun oranı:

$$
P_L=\frac{4}{10}=0{,}4
$$

Sağ grubun oranı:

$$
P_R=\frac{6}{10}=0{,}6
$$

---

### Adım 2 — Sınıf Olasılıklarının Hesaplanması

#### Sol Grup — Yöneticiler

Yöneticilerin 4'ü memnun, 0'ı memnun değildir.

$$
P(Evet|L)=\frac{4}{4}=1
$$

$$
P(Hayır|L)=\frac{0}{4}=0
$$

#### Sağ Grup — Uzmanlar

Uzmanların 2'si memnun, 4'ü memnun değildir.

$$
P(Evet|R)=\frac{2}{6}=\frac{1}{3}
$$

$$
P(Hayır|R)=\frac{4}{6}=\frac{2}{3}
$$

---

### Adım 3 — Sınıf Olasılık Farklarının Hesaplanması

**Evet sınıfı:**

$$
|P(Evet|L)-P(Evet|R)|
$$

$$
=\left|1-\frac{2}{6}\right|
$$

$$
=\frac{4}{6}=\frac{2}{3}
$$

**Hayır sınıfı:**

$$
|P(Hayır|L)-P(Hayır|R)|
$$

$$
=\left|0-\frac{4}{6}\right|
$$

$$
=\frac{4}{6}=\frac{2}{3}
$$

**Toplam mutlak fark:**

$$
\sum_j|P(j|L)-P(j|R)|
$$

$$
=\frac{2}{3}+\frac{2}{3}
$$

$$
=\frac{4}{3}
$$

---

### Adım 4 — Twoing Değerinin Hesaplanması

Twoing formülü:

$$
\Phi=2P_LP_R\sum_j|P(j|L)-P(j|R)|
$$

Değerler yerine yazılır:

$$
\Phi=2(0{,}4)(0{,}6)
\left(\left|1-\frac{2}{6}\right|
+\left|0-\frac{4}{6}\right|\right)
$$

$$
\Phi=2(0{,}4)(0{,}6)
\left(\frac{4}{6}+\frac{4}{6}\right)
$$

$$
\Phi=0{,}48\times\frac{8}{6}
$$

$$
\boxed{\Phi=0{,}64}
$$

---

## 4. Sonuçların Değerlendirilmesi

| Ölçüt | Değer |
|-------|:-----:|
| Toplam çalışan | 10 |
| Sol grup (Yönetici) | 4 |
| Sağ grup (Uzman) | 6 |
| Sol grup oranı | 0,40 |
| Sağ grup oranı | 0,60 |
| Evet sınıfı mutlak farkı | 0,667 |
| Hayır sınıfı mutlak farkı | 0,667 |
| **Twoing değeri** | **0,64** |

### Sonuç

Görev niteliğine göre yapılan bölünmenin Twoing değeri:

$$
\boxed{\Phi=0{,}64}
$$

olarak hesaplanmıştır.

Veri kümesinde:

- Yöneticilerin %100'ü işinden memnundur.
- Uzmanların yaklaşık %33,33'ü işinden memnundur.
- Uzmanların yaklaşık %66,67'si işinden memnun değildir.

Bu sonuç, görev niteliğinin iş memnuniyetini ayırmada yararlı bir özellik olabileceğini göstermektedir.

Twoing değeri **0,64** olduğundan iki grubun sınıf dağılımları arasında belirgin bir farklılık vardır.

Ancak bu bölünmenin en iyi bölünme olduğunu söylemek için diğer özelliklerin Twoing değerleri de hesaplanmalıdır.

**Karar ağacında daha yüksek Twoing değerine sahip bölünme tercih edilir.**
