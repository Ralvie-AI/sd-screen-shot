import time
import logging
import subprocess
import os
import sys
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

SLEEP_THRESHOLD = timedelta(minutes=45)
CHECK_INTERVAL = 5

last_tick_time = None
already_restarted = False

def restart_process(reason: str):
    global already_restarted

    if already_restarted:
        return

    already_restarted = True

    logger.warning(f"Restarting sd-pixel-engine: {reason}")

    try:
        # เปิด process ใหม่
        subprocess.Popen([sys.executable] + sys.argv)

        logger.info("New sd-pixel-engine started.")

        # ปิด process เดิม
        os._exit(0)

    except Exception:
        logger.exception("Failed to restart process")


def sleep_wake_monitor_loop():
    global last_tick_time

    logger.warning("Sleep detector started")

    last_tick_time = datetime.now()

    while True:
        time.sleep(CHECK_INTERVAL)

        now = datetime.now()
        gap = now - last_tick_time

        logger.warning(
            f"last={last_tick_time}, now={now}, gap={gap.total_seconds()}"
        )

        if gap >= SLEEP_THRESHOLD:
            logger.warning("LONG SLEEP DETECTED")

        last_tick_time = now