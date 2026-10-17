# 04 — Sayısal Örneği Doğrulama

Bu uygulama, karar ağacındaki aday bir bölmeyi hem entropi hem Gini ölçütüyle elle çözülebilecek sayılar üzerinden denetler.

## Örnek

Ana düğümde 10 gözlem vardır:

- 6 olumlu
- 4 olumsuz

Aday bölmeden sonra:

- Sol çocuk: 4 olumlu, 1 olumsuz
- Sağ çocuk: 2 olumlu, 3 olumsuz

İki çocukta da 5 gözlem bulunduğu için ağırlıkları `0.5` ve `0.5` olur.

## Beklenen elle çözüm

```text
Ana entropi        = 0.9709505945
Sol entropi        = 0.7219280949
Sağ entropi        = 0.9709505945
Ağırlıklı entropi  = 0.8464393447
Bilgi kazancı      = 0.1245112498
```

Gini için:

```text
Ana Gini           = 0.48
Sol Gini           = 0.32
Sağ Gini           = 0.48
Ağırlıklı Gini     = 0.40
Gini azalması      = 0.08
```

## Çalıştırma

```bash
python uygulamalar/04_sayisal_ornek_dogrulama/app.py
```

Program beklenen değerleri `assert` ile kontrol eder ve `sayisal_dogrulama.json` dosyasına yazar. Herhangi bir hesap uyuşmazsa program hata koduyla durur.

