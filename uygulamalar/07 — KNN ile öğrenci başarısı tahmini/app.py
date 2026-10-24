
from math import sqrt
from collections import Counter

veriler = [
    (1, 2, "Kaldi"),
    (2, 3, "Kaldi"),
    (4, 4, "Gecti"),
    (5, 5, "Gecti"),
    (6, 4, "Gecti")
]

yeni = (3, 4)
k = 3

def oklid(a, b):
    return sqrt(
        (a[0] - b[0]) ** 2
        + (a[1] - b[1]) ** 2
    )

uzakliklar = []

for x1, x2, sinif in veriler:
    mesafe = oklid((x1, x2), yeni)
    uzakliklar.append((mesafe, sinif))

uzakliklar.sort(key=lambda x: x[0])

komsular = uzakliklar[:k]

oylar = Counter(sinif for _, sinif in komsular)
tahmin = oylar.most_common(1)[0][0]

print("En yakin komsular:")
for mesafe, sinif in komsular:
    print(round(mesafe, 2), sinif)

print("Tahmin:", tahmin)
