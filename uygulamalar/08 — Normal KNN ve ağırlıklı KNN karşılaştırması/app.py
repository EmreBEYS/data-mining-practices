
from collections import Counter, defaultdict

komsular = [
    (1, "Evet"),
    (2, "Hayir"),
    (3, "Hayir")
]

# Normal KNN
oylar = Counter(sinif for _, sinif in komsular)
normal_sonuc = oylar.most_common(1)[0][0]

# Agirlikli KNN
agirliklar = defaultdict(float)

for mesafe, sinif in komsular:
    agirlik = 1 / mesafe ** 2
    agirliklar[sinif] += agirlik

agirlikli_sonuc = max(agirliklar, key=agirliklar.get)

print("Normal KNN:", normal_sonuc)
print("Agirlikli KNN:", agirlikli_sonuc)

for sinif, agirlik in agirliklar.items():
    print(sinif, "agirlik:", round(agirlik, 4))
