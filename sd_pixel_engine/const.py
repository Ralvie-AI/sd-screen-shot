import os 
from pathlib import Path

SCREENSHOT_FOLDER_USER = os.path.join(os.environ['LOCALAPPDATA'], "Sundial", "Sundial", "Screenshots", '{user_id}')
SCREENSHOT_FOLDER = os.path.join(os.environ['LOCALAPPDATA'], "Sundial", "Sundial", "Screenshots")

INTERVAL = 30  # seconds

CERT = (
    Path(os.getenv("LOCALAPPDATA"))
    / "Sundial"
    / "Sundial"
    / "tls"
    / "localhost.crt"
)

