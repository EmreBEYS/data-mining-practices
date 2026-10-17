"""Eğitim amaçlı kredi riski verisiyle karar ağacı oluşturur."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree


def kredi_verisi() -> pd.DataFrame:
    """Tamamen eğitim amacıyla oluşturulmuş küçük ve sentetik veri kümesi."""
    kayitlar = [
        (22, 18000, "hayir", "yuksek", "yuksek"),
        (25, 24000, "evet", "yuksek", "yuksek"),
        (28, 32000, "evet", "orta", "orta"),
        (31, 41000, "evet", "dusuk", "dusuk"),
        (35, 52000, "evet", "dusuk", "dusuk"),
        (42, 47000, "evet", "orta", "dusuk"),
        (46, 29000, "hayir", "yuksek", "yuksek"),
        (52, 65000, "evet", "dusuk", "dusuk"),
        (23, 27000, "hayir", "orta", "yuksek"),
        (39, 38000, "evet", "yuksek", "orta"),
        (48, 56000, "evet", "orta", "dusuk"),
        (55, 34000, "hayir", "orta", "orta"),
        (29, 45000, "evet", "dusuk", "dusuk"),
        (33, 26000, "evet", "yuksek", "yuksek"),
        (44, 72000, "evet", "dusuk", "dusuk"),
        (50, 40000, "hayir", "yuksek", "yuksek"),
        (37, 61000, "evet", "orta", "dusuk"),
        (27, 36000, "evet", "orta", "orta"),
        (58, 50000, "evet", "yuksek", "orta"),
        (40, 23000, "hayir", "yuksek", "yuksek"),
    ]
    return pd.DataFrame(
        kayitlar,
        columns=["yas", "gelir", "duzenli_is", "borc_orani", "kredi_riski"],
    )


def model_olustur() -> Pipeline:
    kategorik = ["duzenli_is", "borc_orani"]
    on_isleme = ColumnTransformer(
        [("kategorik", OneHotEncoder(handle_unknown="ignore"), kategorik)],
        remainder="passthrough",
        verbose_feature_names_out=False,
    )
    agac = DecisionTreeClassifier(
        criterion="entropy", max_depth=4, min_samples_leaf=2, random_state=42
    )
    return Pipeline([("on_isleme", on_isleme), ("agac", agac)])


def calistir(output_dir: Path) -> tuple[Pipeline, float]:
    veri = kredi_verisi()
    x = veri.drop(columns="kredi_riski")
    y = veri["kredi_riski"]
    model = model_olustur()
    model.fit(x, y)
    dogruluk = model.score(x, y)

    output_dir.mkdir(parents=True, exist_ok=True)
    veri.to_csv(output_dir / "kredi_riski_verisi.csv", index=False)

    on_isleme = model.named_steps["on_isleme"]
    agac = model.named_steps["agac"]
    ozellik_adlari = on_isleme.get_feature_names_out()

    fig, ax = plt.subplots(figsize=(17, 8))
    plot_tree(
        agac,
        feature_names=ozellik_adlari,
        class_names=[str(deger) for deger in agac.classes_],
        filled=True,
        rounded=True,
        impurity=True,
        proportion=True,
        ax=ax,
    )
    ax.set_title("Eğitim Amaçlı Kredi Riski Karar Ağacı")
    fig.tight_layout()
    fig.savefig(output_dir / "kredi_riski_karar_agaci.png", dpi=170)
    plt.close(fig)

    kurallar = export_text(agac, feature_names=list(ozellik_adlari))
    (output_dir / "karar_kurallari.txt").write_text(kurallar, encoding="utf-8")

    ornek = pd.DataFrame(
        [{"yas": 30, "gelir": 39000, "duzenli_is": "evet", "borc_orani": "orta"}]
    )
    tahmin = model.predict(ornek)[0]
    print(f"Eğitim doğruluğu: {dogruluk:.3f}")
    print(f"Örnek müşteri için tahmin edilen risk: {tahmin}")
    print("Not: Sonuçlar yalnızca eğitim amaçlıdır.")
    return model, dogruluk


def argumanlar() -> argparse.Namespace:
    varsayilan = Path(__file__).resolve().parent / "sonuclar"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=varsayilan)
    return parser.parse_args()


if __name__ == "__main__":
    calistir(argumanlar().output_dir)

