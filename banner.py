import os
from core.colors import Colors as C

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_banner():
    clear()
    print(f"""{C.R}{C.BT}
  _   _             _____      _ _   _  __ _ _ _           
 | |_| |__   ___   | ____|_   _(_) | | |/ /(_) | | ___ _ __ 
 | __| '_ \ / _ \  |  _| \ \ / / | | | ' / | | | |/ _ \ '__|
 | |_| | | |  __/  | |___ \ V /| | | | . \ | | | |  __/ |   
  \__|_| |_|\___|  |_____| \_/ |_|_| |_|\_\|_|_|_|\___|_|
    {C.W}──────────────────────────────────────────────────────────
    {C.C}ENGINE: {C.W}V3.4.0-PRO  {C.C}|  XPL PROJECT {C.Y}[STABLE]
    {C.C}STATUS: {C.G}LISTENING FOR TARGET PAYLOADS...
    {C.W}──────────────────────────────────────────────────────────""")
