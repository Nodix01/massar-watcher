"""
Massar availability watcher
----------------------------
Pings the Massar login page every ~60-90s (backing off if it keeps failing)
until it responds normally instead of connection-reset/timeout, then alerts
you so you can go log in and check your grades.

This project only checks whether the Massar portal is reachable.

It never logs into accounts, accesses personal information,
or interacts with student data.

Usage:
    pip install requests
    python watcher.py
    (Ctrl+C to stop anytime)
"""

import requests
import time
import random
import sys
from datetime import datetime

# ----------------------- Configuration -----------------------
URL = "https://massarservice.men.gov.ma/moutamadris"
BASE_INTERVAL = 60      # seconds between checks when things are going well
MAX_INTERVAL = 300      # cap on the exponential backoff
BACKOFF_FACTOR = 1.4    # how fast the interval grows after each failure
TIMEOUT = 10            # seconds to wait for a response before giving up
LOG_FILE = "massar_watch.log"

# Optional: paste a Discord webhook URL here to also get notified on your phone.
# Leave empty and you still get console output + a beep.
DISCORD_WEBHOOK = ""
# ----------------------------------------------------------------


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass  # a logging hiccup shouldn't kill the watcher


def notify_discord(message):
    if not DISCORD_WEBHOOK:
        return
    try:
        requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=5)
    except requests.exceptions.RequestException:
        pass  # don't let a failed notification crash the loop


def beep():
    try:
        import winsound
        winsound.Beep(1000, 400)
        winsound.Beep(1300, 400)
    except ImportError:
        print("\a")  # fallback terminal bell on non-Windows (may be silent depending on terminal settings)


def check_once():
    """Returns (is_up, detail) without ever touching login/credentials."""
    try:
        resp = requests.get(URL, timeout=TIMEOUT)
        if resp.ok:  # 2xx/3xx only - a 502/503 during heavy load is NOT "up"
            return True, f"HTTP {resp.status_code}"
        return False, f"HTTP {resp.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "connection reset/refused"
    except requests.exceptions.Timeout:
        return False, "timeout"
    except requests.exceptions.RequestException as e:
        return False, f"error: {e.__class__.__name__}"


def main():
    log(f"Watching {URL}")
    log(f"Checking every {BASE_INTERVAL}-{MAX_INTERVAL}s, backing off on repeated failures. Ctrl+C to stop.")

    interval = BASE_INTERVAL
    attempt = 0

    while True:
        attempt += 1
        up, detail = check_once()

        if up:
            log(f"UP after {attempt} check(s) - {detail}")
            message = f"Massar is reachable again ({detail}) - go log in and check your grades."
            log(message)
            notify_discord(message)
            beep()
            break
        else:
            log(f"still down (#{attempt}) - {detail}, next check in ~{int(interval)}s")

        sleep_time = interval + random.uniform(-10, 10)
        time.sleep(max(20, sleep_time))
        interval = min(interval * BACKOFF_FACTOR, MAX_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Stopped by user.")
        sys.exit(0)
