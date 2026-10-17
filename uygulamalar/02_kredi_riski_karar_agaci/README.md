# 02 — Kredi Riski Karar Ağacı

Bu uygulama küçük, sentetik bir veri kümesinden kredi riski sınıflandırma ağacı kurar. Kategorik sütunlar one-hot encoding ile dönüştürülür; sayısal sütunlar doğrudan kullanılır.

> Bu örnek gerçek kredi değerlendirmesi için uygun değildir. Veri ve çıktı yalnızca eğitim amacı taşır.

## Kullanılan değişkenler

- `yas`: Müşterinin yaşı
- `gelir`: Yıllık örnek gelir
- `duzenli_is`: Düzenli iş bilgisi
- `borc_orani`: Düşük, orta veya yüksek borç oranı
- `kredi_riski`: Tahmin edilmek istenen sınıf

## Çalıştırma

```bash
python uygulamalar/02_kredi_riski_karar_agaci/app.py
```

## Üretilen dosyalar

- `kredi_riski_verisi.csv`: Örnekte kullanılan sentetik veri
- `kredi_riski_karar_agaci.png`: Ağacın görselleştirmesi
- `karar_kurallari.txt`: Ağacın metin biçimindeki kuralları

Kodda `Pipeline` kullanıldığı için, tahmin sırasında eğitimdeki dönüşümlerin aynısı otomatik uygulanır. `random_state=42` sonucu tekrarlanabilir kılar.

