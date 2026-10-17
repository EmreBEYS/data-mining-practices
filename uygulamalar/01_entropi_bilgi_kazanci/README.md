# 01 — Entropi ve Bilgi Kazancı

Bu uygulama klasik **Tenis Oyna** veri kümesindeki hedef entropisini ve dört kategorik özniteliğin bilgi kazancını, hazır bir karar ağacı sınıfı kullanmadan hesaplar.

## Formüller

Sınıf olasılıkları \(p_i\) olmak üzere entropi:

```text
H(S) = -Σ pᵢ log₂(pᵢ)
```

Bir `A` özniteliğinin bilgi kazancı:

```text
IG(S, A) = H(S) - Σ (|Sᵥ| / |S|) H(Sᵥ)
```

## Çalıştırma

Depo ana klasöründeyken:

```bash
python uygulamalar/01_entropi_bilgi_kazanci/app.py
```

## Beklenen sonuç

- Hedef entropisi: yaklaşık `0.940286` bit
- En yüksek bilgi kazancı: `hava`, yaklaşık `0.246750` bit
- Ardından sırasıyla `nem`, `ruzgar` ve `sicaklik`

Program `bilgi_kazanci.csv` tablosunu ve `bilgi_kazanci.png` grafiğini üretir.

