"""Depodaki dört ders uygulaması için temel bütünlük testleri."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path


KOK = Path(__file__).resolve().parents[1]


def modul_yukle(ad: str, yol: Path):
    spec = importlib.util.spec_from_file_location(ad, yol)
    assert spec and spec.loader
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def test_entropi_ve_bilgi_kazanci(tmp_path: Path) -> None:
    modul = modul_yukle(
        "entropi_app", KOK / "uygulamalar/01_entropi_bilgi_kazanci/app.py"
    )
    sonuclar = modul.calistir(tmp_path)
    assert sonuclar.iloc[0]["ozellik"] == "hava"
    assert math.isclose(sonuclar.iloc[0]["bilgi_kazanci"], 0.2467498198, abs_tol=1e-9)
    assert (tmp_path / "bilgi_kazanci.png").stat().st_size > 0


def test_kredi_riski_agaci(tmp_path: Path) -> None:
    modul = modul_yukle(
        "kredi_app", KOK / "uygulamalar/02_kredi_riski_karar_agaci/app.py"
    )
    _, dogruluk = modul.calistir(tmp_path)
    assert dogruluk >= 0.85
    assert (tmp_path / "kredi_riski_karar_agaci.png").stat().st_size > 0
    assert (tmp_path / "karar_kurallari.txt").stat().st_size > 0


def test_iris_degerlendirme(tmp_path: Path) -> None:
    modul = modul_yukle(
        "iris_app", KOK / "uygulamalar/03_iris_egitim_test_confusion_matrix/app.py"
    )
    dogruluk, matris = modul.calistir(tmp_path)
    assert dogruluk >= 0.90
    assert matris.to_numpy().sum() == 45
    assert (tmp_path / "confusion_matrix.png").stat().st_size > 0


def test_sayisal_ornek(tmp_path: Path) -> None:
    modul = modul_yukle(
        "sayisal_app", KOK / "uygulamalar/04_sayisal_ornek_dogrulama/app.py"
    )
    sonuclar = modul.calistir(tmp_path)
    assert math.isclose(sonuclar["bilgi_kazanci"], 0.1245112498, abs_tol=1e-10)
    assert math.isclose(sonuclar["gini_azalmasi"], 0.08, abs_tol=1e-12)
    assert (tmp_path / "sayisal_dogrulama.json").stat().st_size > 0

