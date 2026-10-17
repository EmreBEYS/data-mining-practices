"""Iris verisini eğitim-test kümelerine ayırır ve hata matrisini çizer."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def calistir(output_dir: Path) -> tuple[float, pd.DataFrame]:
    iris = load_iris(as_frame=True)
    x = iris.data
    y = iris.target
    x_egitim, x_test, y_egitim, y_test = train_test_split(
        x,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y,
    )

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(x_egitim, y_egitim)
    tahmin = model.predict(x_test)
    dogruluk = accuracy_score(y_test, tahmin)
    matris = confusion_matrix(y_test, tahmin)
    matris_df = pd.DataFrame(matris, index=iris.target_names, columns=iris.target_names)

    output_dir.mkdir(parents=True, exist_ok=True)
    matris_df.to_csv(output_dir / "confusion_matrix.csv")
    rapor = classification_report(
        y_test,
        tahmin,
        target_names=iris.target_names,
        digits=4,
        zero_division=0,
    )
    (output_dir / "siniflandirma_raporu.txt").write_text(rapor, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7, 6))
    gosterim = ConfusionMatrixDisplay(matris, display_labels=iris.target_names)
    gosterim.plot(cmap="Blues", values_format="d", ax=ax, colorbar=False)
    ax.set_title(f"Iris Hata Matrisi — Doğruluk: {dogruluk:.3f}")
    ax.set_xlabel("Tahmin edilen sınıf")
    ax.set_ylabel("Gerçek sınıf")
    fig.tight_layout()
    fig.savefig(output_dir / "confusion_matrix.png", dpi=170)
    plt.close(fig)

    print(f"Eğitim örneği: {len(x_egitim)}")
    print(f"Test örneği: {len(x_test)}")
    print(f"Doğruluk: {dogruluk:.4f}")
    print(rapor)
    return dogruluk, matris_df


def argumanlar() -> argparse.Namespace:
    varsayilan = Path(__file__).resolve().parent / "sonuclar"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=varsayilan)
    return parser.parse_args()


if __name__ == "__main__":
    calistir(argumanlar().output_dir)

