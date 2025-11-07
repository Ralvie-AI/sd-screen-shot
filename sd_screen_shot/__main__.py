import argparse
from datetime import time

from sd_screen_shot.screenshot import ScreenShot
# from screenshot import ScreenShot

def parse_time(value: str) -> time:
    try:
        hour, minute = map(int, value.split(":"))
        return time(hour, minute)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid time format: '{value}'. Use HH:MM (e.g., 09:00)"
        )

def parse_days(value):
    try:
        return [int(v) for v in value.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError("Days must be comma-separated integers (e.g. 0,1,2,3,4)")
    
def main():
    parser = argparse.ArgumentParser(description="Screenshot uploader")
    parser.add_argument("--server_url", required=True, help="URL to upload screenshots")
    parser.add_argument("--user_id", required=True, help="User ID for identification")
    parser.add_argument("--start_hour", type=parse_time, default=time(8, 0),
                    help="Start time (HH:MM)")
    parser.add_argument("--end_hour", type=parse_time, default=time(17, 0),
                    help="End time (HH:MM)")
    parser.add_argument("--times_per_hour", type=int, default=7, help="Screenshots per hour")
    parser.add_argument("--days", type=parse_days, default=[0,1,2,3,4], help="Allowed weekdays (0=Mon ... 6=Sun)")

    args = parser.parse_args()

    print("args ", args)

    screenshot = ScreenShot(
        server_url=args.server_url,
        user_id=args.user_id,
        start_time=args.start_hour,
        end_time=args.end_hour,
        times_per_hour=args.times_per_hour,
        days=args.days
    )

    screenshot.run()

if __name__ == '__main__':
    main()