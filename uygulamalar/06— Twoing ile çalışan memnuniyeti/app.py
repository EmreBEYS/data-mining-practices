
def twoing(sol, sag):
    toplam = len(sol) + len(sag)

    p_sol = len(sol) / toplam
    p_sag = len(sag) / toplam

    siniflar = set(sol + sag)

    fark_toplami = 0

    for sinif in siniflar:
        olasilik_sol = sol.count(sinif) / len(sol)
        olasilik_sag = sag.count(sinif) / len(sag)

        fark_toplami += abs(
            olasilik_sol - olasilik_sag
        )

    return 2 * p_sol * p_sag * fark_toplami

yoneticiler = ["Evet"] * 4
uzmanlar = ["Evet"] * 2 + ["Hayir"] * 4

sonuc = twoing(yoneticiler, uzmanlar)
print("Twoing sonucu: ", sonuc)
