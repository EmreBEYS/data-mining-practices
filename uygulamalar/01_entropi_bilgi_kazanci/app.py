"""Kategorik öznitelikler için entropi ve bilgi kazancı hesabı."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def entropi(degerler: pd.Series) -> float:
    """Bir sınıf sütununun Shannon entropisini hesaplar."""
    oranlar = degerler.value_counts(normalize=True)
    return -sum(oran * math.log2(oran) for oran in oranlar if oran > 0)


def bilgi_kazanci(veri: pd.DataFrame, ozellik: str, hedef: str) -> float:
    """Kategorik bir özellik için bilgi kazancını döndürür."""
    ana_entropi = entropi(veri[hedef])
    agirlikli_entropi = 0.0
    for _, grup in veri.groupby(ozellik, observed=True):
        agirlikli_entropi += len(grup) / len(veri) * entropi(grup[hedef])
    return ana_entropi - agirlikli_entropi


def oyun_verisi() -> pd.DataFrame:
    """Klasik 14 satırlık 'tenis oyna' veri kümesini Türkçe sunar."""
    return pd.DataFrame(
        {
            "hava": [
                "gunesli", "gunesli", "bulutlu", "yagmurlu", "yagmurlu", "yagmurlu", "bulutlu",
                "gunesli", "gunesli", "yagmurlu", "gunesli", "bulutlu", "bulutlu", "yagmurlu",
            ],
            "sicaklik": [
                "sicak", "sicak", "sicak", "ilik", "serin", "serin", "serin",
                "ilik", "serin", "ilik", "ilik", "ilik", "sicak", "ilik",
            ],
            "nem": [
                "yuksek", "yuksek", "yuksek", "yuksek", "normal", "normal", "normal",
                "yuksek", "normal", "normal", "normal", "yuksek", "normal", "yuksek",
            ],
            "ruzgar": [
                "zayif", "guclu", "zayif", "zayif", "zayif", "guclu", "guclu",
                "zayif", "zayif", "zayif", "guclu", "guclu", "zayif", "guclu",
            ],
            "oyna": [
                "hayir", "hayir", "evet", "evet", "evet", "hayir", "evet",
                "hayir", "evet", "evet", "evet", "evet", "evet", "hayir",
            ],
        }
    )


def calistir(output_dir: Path) -> pd.DataFrame:
    veri = oyun_verisi()
    ozellikler = [sutun for sutun in veri.columns if sutun != "oyna"]
    sonuclar = pd.DataFrame(
        {
            "ozellik": ozellikler,
            "bilgi_kazanci": [bilgi_kazanci(veri, sutun, "oyna") for sutun in ozellikler],
        }
    ).sort_values("bilgi_kazanci", ascending=False, ignore_index=True)

    output_dir.mkdir(parents=True, exist_ok=True)
    sonuclar.to_csv(output_dir / "bilgi_kazanci.csv", index=False, float_format="%.6f")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(sonuclar["ozellik"], sonuclar["bilgi_kazanci"], color="#3572A5")
    ax.set_title("Özniteliklere Göre Bilgi Kazancı")
    ax.set_xlabel("Öznitelik")
    ax.set_ylabel("Bilgi kazancı (bit)")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "bilgi_kazanci.png", dpi=160)
    plt.close(fig)

    print(f"Hedef entropisi: {entropi(veri['oyna']):.6f} bit")
    print(sonuclar.to_string(index=False, formatters={"bilgi_kazanci": "{:.6f}".format}))
    print(f"En iyi ilk bölme: {sonuclar.iloc[0]['ozellik']}")
    return sonuclar


def argumanlar() -> argparse.Namespace:
    varsayilan = Path(__file__).resolve().parent / "sonuclar"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=varsayilan)
    return parser.parse_args()


if __name__ == "__main__":
    calistir(argumanlar().output_dir)

