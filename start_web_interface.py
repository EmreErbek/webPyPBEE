#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyPBEE Türkçe Web Arayüzü Başlatıcı

Bu script, Streamlit web arayüzünü başlatır.

Kullanım:
    python start_web_interface.py
"""

import subprocess
import sys
import os
from pathlib import Path

def check_requirements():
    """Gerekli paketlerin yüklü olup olmadığını kontrol et"""
    try:
        import streamlit
        import pandas
        import matplotlib
        import numpy
        print("✅ Tüm gerekli paketler yüklü")
        return True
    except ImportError as e:
        print(f"❌ Eksik paket: {e.name}")
        print("\nGerekli paketleri yüklemek için:")
        print("  pip install -r requirements.txt")
        return False

def start_streamlit():
    """Streamlit arayüzünü başlat"""
    script_dir = Path(__file__).parent
    interface_path = script_dir / "web_interface.py"

    if not interface_path.exists():
        print(f"❌ Hata: {interface_path} bulunamadı")
        return False

    print("\n" + "="*60)
    print("🏗️  PyPBEE Türkçe Web Arayüzü Başlatılıyor...")
    print("="*60 + "\n")

    print("📍 Arayüz konumu:", interface_path)
    print("🌐 Tarayıcınızda otomatik olarak açılacak...")
    print("🔗 Manuel olarak: http://localhost:8501")
    print("\n⚠️  Kapatmak için: Ctrl+C (veya Cmd+C Mac'te)\n")
    print("="*60 + "\n")

    try:
        # Streamlit'i başlat
        subprocess.run([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(interface_path),
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
        return True
    except KeyboardInterrupt:
        print("\n\n✋ Arayüz kapatıldı. Güle güle!")
        return True
    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")
        return False

def main():
    """Ana fonksiyon"""
    print("\n🚀 PyPBEE Türkçe Web Arayüzü Başlatıcı\n")

    # Gerekli paketleri kontrol et
    if not check_requirements():
        sys.exit(1)

    # Streamlit'i başlat
    if not start_streamlit():
        sys.exit(1)

if __name__ == "__main__":
    main()
