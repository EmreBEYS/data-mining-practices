"""Elle çözülebilen bir bölme örneğini sayısal olarak doğrular."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def ikili_entropi(pozitif: int, negatif: int) -> float:
    toplam = pozitif + negatif
    if toplam == 0:
        return 0.0
    sonuc = 0.0
    for adet in (pozitif, negatif):
        if adet:
            oran = adet / toplam
            sonuc -= oran * math.log2(oran)
    return sonuc


def gini(pozitif: int, negatif: int) -> float:
    toplam = pozitif + negatif
    if toplam == 0:
        return 0.0
    return 1 - (pozitif / toplam) ** 2 - (negatif / toplam) ** 2


def hesapla() -> dict[str, float]:
    # Ana düğüm: 6 olumlu, 4 olumsuz.
    # Bölme sonrası sol: 4/1, sağ: 2/3; her çocukta 5 örnek vardır.
    ana_entropi = ikili_entropi(6, 4)
    sol_entropi = ikili_entropi(4, 1)
    sag_entropi = ikili_entropi(2, 3)
    agirlikli_entropi = 0.5 * sol_entropi + 0.5 * sag_entropi

    ana_gini = gini(6, 4)
    agirlikli_gini = 0.5 * gini(4, 1) + 0.5 * gini(2, 3)
    return {
        "ana_entropi": ana_entropi,
        "sol_entropi": sol_entropi,
        "sag_entropi": sag_entropi,
        "agirlikli_cocuk_entropisi": agirlikli_entropi,
        "bilgi_kazanci": ana_entropi - agirlikli_entropi,
        "ana_gini": ana_gini,
        "agirlikli_cocuk_ginisi": agirlikli_gini,
        "gini_azalmasi": ana_gini - agirlikli_gini,
    }


def calistir(output_dir: Path) -> dict[str, float]:
    sonuclar = hesapla()
    # Ders notundaki elle hesaplanan değerleri toleransla doğrula.
    assert math.isclose(sonuclar["ana_entropi"], 0.9709505945, abs_tol=1e-10)
    assert math.isclose(sonuclar["bilgi_kazanci"], 0.1245112498, abs_tol=1e-10)
    assert math.isclose(sonuclar["gini_azalmasi"], 0.08, abs_tol=1e-12)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "sayisal_dogrulama.json").write_text(
        json.dumps(sonuclar, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Sayısal örnek başarıyla doğrulandı.")
    for ad, deger in sonuclar.items():
        print(f"{ad}: {deger:.10f}")
    return sonuclar


def argumanlar() -> argparse.Namespace:
    varsayilan = Path(__file__).resolve().parent / "sonuclar"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=varsayilan)
    return parser.parse_args()


if __name__ == "__main__":
    calistir(argumanlar().output_dir)

