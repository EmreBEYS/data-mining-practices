# Veri Madenciliği Ders Uygulamaları

Bu depo, veri madenciliğinin temel sınıflandırma ve karar ağacı konularını Python ile uygulamalı biçimde incelemek için hazırlanmıştır. Her uygulama bağımsız çalışır, sabit bir rastgelelik tohumu kullanır ve elde ettiği sonuçları belirtilen klasöre kaydeder.

## İçerik

| No | Uygulama | Öğrenme amacı |
|---:|---|---|
| 1 | [Entropi ve bilgi kazancı](uygulamalar/01_entropi_bilgi_kazanci/README.md) | Entropiyi ve kategorik özniteliklerin bilgi kazancını sıfırdan hesaplamak |
| 2 | [Kredi riski karar ağacı](uygulamalar/02_kredi_riski_karar_agaci/README.md) | Kategorik ve sayısal verilerle karar ağacı kurmak ve görselleştirmek |
| 3 | [Iris eğitim-test ve confusion matrix](uygulamalar/03_iris_egitim_test_confusion_matrix/README.md) | Stratified veri bölme, model değerlendirme ve hata matrisi üretmek |
| 4 | [Sayısal örneği doğrulama](uygulamalar/04_sayisal_ornek_dogrulama/README.md) | Elle çözülen entropi, bilgi kazancı ve Gini azalmasını kodla doğrulamak |

## Kurulum

Python 3.10 veya daha yeni bir sürüm önerilir.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS / Linux:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Uygulamaları çalıştırma

Komutları depo ana klasöründe çalıştırın:

```bash
python uygulamalar/01_entropi_bilgi_kazanci/app.py
python uygulamalar/02_kredi_riski_karar_agaci/app.py
python uygulamalar/03_iris_egitim_test_confusion_matrix/app.py
python uygulamalar/04_sayisal_ornek_dogrulama/app.py
```

Her program varsayılan olarak kendi klasörü altında `sonuclar/` oluşturur. Başka bir hedef seçmek için:

```bash
python uygulamalar/03_iris_egitim_test_confusion_matrix/app.py --output-dir kendi_sonuclarim
```

## Testler

```bash
python -m pytest -q
```

Testler temel matematiksel sonuçları, oluşturulan model dosyalarını ve görselleri denetler. Örnek çalıştırma çıktıları `ornek_ciktilar/` klasörlerinde ayrıca depoya eklenmiştir.

## Kullanılan kavramlar

- **Entropi:** Bir sınıf dağılımındaki belirsizliği ölçer. Saf düğümde 0'dır.
- **Bilgi kazancı:** Bölme öncesi entropi ile ağırlıklı çocuk entropileri arasındaki farktır.
- **Gini safsızlığı:** Karar ağaçlarında sık kullanılan başka bir safsızlık ölçüsüdür.
- **Stratified ayırma:** Eğitim ve test kümelerinde sınıf oranlarını korur.
- **Confusion matrix (hata matrisi):** Gerçek ve tahmin edilen sınıfları karşılaştırır.

## Not

Bu veri kümeleri eğitim amacıyla küçük ve anlaşılır tutulmuştur. Kredi riski örneği gerçek bir kredi kararı vermek için kullanılamaz; yalnızca karar ağacının çalışma biçimini gösterir.

