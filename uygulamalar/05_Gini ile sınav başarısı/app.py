def gini(siniflar):
    toplam = len(siniflar)
    if toplam == 0:
        return 0.0
    return 1.0 - sum((siniflar.count(sinif) / toplam) ** 2 for sinif in set(siniflar))

duzenli = ["Gecti", "Gecti", "Gecti", "Kaldi"]
duzensiz = ["Gecti", "Kaldi", "Kaldi", "Kaldi"]

sol = gini(duzenli)
sag = gini(duzensiz)

n=len(duzenli) + len(duzensiz)
agirlikli_gini = (len(duzenli) / n) * sol + (len(duzensiz) / n) * sag

print("Düzenli Gini: ", sol)
print("Düzensiz Gini: ", sag)
print("Ağırlıklı Gini: ", agirlikli_gini)