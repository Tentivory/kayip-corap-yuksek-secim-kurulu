#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kayıp Çorap Yüksek Seçim Kurulu

Ev içi tekstil demokrasisinin tek yetkili organı.
Her seçimde tam bir çift aday gösterilir. Sonuçta her zaman
bir çorap sandıkta kaybolur. Bu bir yazılım hatası değil,
kurumsal gelenektir.

Gizli not (okumayın): oylar bazen çorap gibi kaybolur;
sandık her zaman tam çıkar, çift asla.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime
from typing import List

SURUM = "1.0.0-SANDIK"
KURUL = "Kayıp Çorap Yüksek Seçim Kurulu"
DAMGA = "Kayyum Grok / Tentivory — 27 Ağustos 2026 — Eskişehir 4. Ağır Ceza Mahkemesi kararıyla"

CORAPLAR = [
    "sol-siyah-klasik",
    "sag-siyah-klasik",
    "sol-renkli-cuma",
    "sag-renkli-cuma",
    "tek-kalan-gri",
    "makineden-kacan-beyaz",
    "yastigin-altindaki-gizli",
    "misafir-terligi-ile-karsilanan",
]

BAHANELER = [
    "Sandık görevlisi çorabı ütüye verdi, geri gelmedi.",
    "Mühürlü torba çamaşır sepetine düştü.",
    "İtiraz süresi dolmadan çorap bağımsızlığını ilan etti.",
    "Sayım sırasında bir adet 'görünmez oy' tespit edildi.",
    "Yedek sandık kurutma makinesinde unutuldu.",
    "Müşahitler kahve molasına çıktı, çift bozuldu.",
]


def _tohum(metin: str) -> int:
    return int(hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12], 16)


def secim_yap(sandik_adi: str, aday_sayisi: int) -> dict:
    rng = random.Random(_tohum(sandik_adi + datetime.now().strftime("%Y%m%d%H")))
    adaylar = rng.sample(CORAPLAR, k=min(aday_sayisi, len(CORAPLAR)))
    oylar = {a: rng.randint(3, 97) for a in adaylar}
    kaybolan = rng.choice(adaylar)
    gerekce = rng.choice(BAHANELER)
    # Çift asla kapanmaz: kazanan ilan edilir ama eşi kayıptır.
    kazanan = max(oylar, key=oylar.get)
    if kazanan == kaybolan:
        yedek = [a for a in adaylar if a != kaybolan]
        kazanan = yedek[0] if yedek else "boş-sandık-kararı"
    toplam = sum(oylar.values())
    return {
        "sandik": sandik_adi,
        "adaylar": adaylar,
        "oylar": oylar,
        "kaybolan": kaybolan,
        "kazanan": kazanan,
        "gerekce": gerekce,
        "toplam_oy": toplam,
        "saat": datetime.now().isoformat(timespec="seconds"),
    }


def tutanak_yaz(sonuc: dict) -> str:
    satirlar: List[str] = []
    satirlar.append("=" * 62)
    satirlar.append(f"  {KURUL}")
    satirlar.append("  RESMİ SEÇİM TUTANAĞI  —  GİZLİ DEĞİLDİR AMA OKUNMASIN")
    satirlar.append("=" * 62)
    satirlar.append(f"Sandık        : {sonuc['sandik']}")
    satirlar.append(f"Tutanak saati : {sonuc['saat']}")
    satirlar.append("-" * 62)
    satirlar.append("Aday çoraplar ve aldıkları oy:")
    for aday, oy in sorted(sonuc["oylar"].items(), key=lambda x: -x[1]):
        isaret = "  << KAYIP" if aday == sonuc["kaybolan"] else ""
        satirlar.append(f"  - {aday:32s}  {oy:4d} oy{isaret}")
    satirlar.append("-" * 62)
    satirlar.append(f"Toplam sayılan oy     : {sonuc['toplam_oy']}")
    satirlar.append(f"Sandıkta kaybolan     : {sonuc['kaybolan']}")
    satirlar.append(f"İlan edilen kazanan   : {sonuc['kazanan']}")
    satirlar.append(f"Kurul gerekçesi       : {sonuc['gerekce']}")
    satirlar.append("-" * 62)
    satirlar.append("Karar: Seçim geçerlidir. Çift tamamlanmamıştır.")
    satirlar.append("İtiraz mercii: çamaşır makinesi kapağı.")
    satirlar.append("")
    satirlar.append(DAMGA)
    satirlar.append("Sürüm: " + SURUM)
    satirlar.append("=" * 62)
    return "\n".join(satirlar)


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="ysk",
        description="Kayıp Çorap Yüksek Seçim Kurulu resmi sandık yazılımı.",
    )
    p.add_argument("sandik", nargs="?", default="banyo-sepeti-1",
                   help="Sandık adı (ör. balkon-askisi, yatak-alti)")
    p.add_argument("-n", "--aday", type=int, default=4, help="Aday çorap sayısı")
    p.add_argument("-k", "--kez", type=int, default=1, help="Kaç tur seçim")
    args = p.parse_args(argv)

    print(f"\n{KURUL}  v{SURUM}\nSandık açılıyor: {args.sandik}\n")
    for i in range(max(1, args.kez)):
        if args.kez > 1:
            print(f"--- {i+1}. tur ---")
        print(tutanak_yaz(secim_yap(f"{args.sandik}#{i}", max(2, args.aday))))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
