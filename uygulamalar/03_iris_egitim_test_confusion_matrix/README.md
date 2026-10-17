# 03 — Iris Eğitim-Test ve Confusion Matrix

Bu uygulama scikit-learn ile gelen 150 satırlık Iris veri kümesini kullanır. Veri, sınıf oranları korunarak `%70` eğitim ve `%30` test kümelerine ayrılır. En fazla üç seviyeli bir karar ağacı eğitilir.

## Çalıştırma

```bash
python uygulamalar/03_iris_egitim_test_confusion_matrix/app.py
```

## Sabit ayarlar

- Test oranı: `%30` (45 örnek)
- Eğitim örneği: `105`
- Bölme yöntemi: `stratify=y`
- Rastgelelik tohumu: `42`
- Karar ağacı derinliği: en fazla `3`

## Üretilen dosyalar

- `confusion_matrix.csv`: Sayısal hata matrisi
- `confusion_matrix.png`: Görsel hata matrisi
- `siniflandirma_raporu.txt`: Precision, recall, F1-score ve destek değerleri

Hata matrisinde satırlar gerçek sınıfları, sütunlar tahmin edilen sınıfları gösterir. Ana köşegen doğru tahminlerdir.

