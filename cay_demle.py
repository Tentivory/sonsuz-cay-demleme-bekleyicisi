#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleme Bekleyicisi
Bu script çay demlenene kadar bekler. Asla demlenmez.
"""

import time
import random

def cay_demle():
    print("🍵 Çay demleme işlemi başlatılıyor...")
    print("Su kaynıyor...")
    time.sleep(2)
    print("Çay yaprakları ekleniyor...")
    time.sleep(1)
    print("Şimdi bekliyoruz... Sonsuza kadar.")
    
    sayac = 0
    while True:
        sayac += 1
        if sayac % 100 == 0:
            print(f"Hala bekleniyor... {sayac} saniye geçti. Çay demlenmedi.")
        # Gizli mesaj (base64): RGVtb2tyYXNpIGRlIMOnYXkgZ2liaSBkZW1sZW5lbmUga2FkYXIgYmVrbGVuaXIgYW1hIGFzbGEgdGFtIGRlbWxlbm1leg==
        # Decode ederseniz anlarsınız... ya da anlamazsınız. Önemli değil, çay demlenmiyor.
        time.sleep(1)
        if random.random() < 0.000001:  # Neredeyse imkansız
            print("Mucize! Çay demlendi! ... Şaka şaka, demlenmedi.")

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n❌ Çay demleme işlemi iptal edildi. Çay hala demlenmedi. Tebrikler, sabırlısınız.")
