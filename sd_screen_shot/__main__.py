import argparse
from datetime import time

from sd_screen_shot.screenshot import ScreenShot
# from screenshot import ScreenShot

def main():
    parser = argparse.ArgumentParser(description="Screenshot uploader")
    parser.add_argument("--server_url", required=True, help="URL to upload screenshots")
    parser.add_argument("--user_id", required=True, help="User ID for identification")
    parser.add_argument("--start_hour", type=int, default=8, help="Start time hour")
    parser.add_argument("--end_hour", type=int, default=17, help="End time hour")
    parser.add_argument("--times_per_hour", type=int, default=7, help="Screenshots per hour")
    parser.add_argument("--days", nargs="+", type=int, default=[0,1,2,3,4], help="Allowed weekdays (0=Mon ... 6=Sun)")

    args = parser.parse_args()

    print("args ", args)

    screenshot = ScreenShot(
        server_url=args.server_url,
        user_id=args.user_id,
        start_time=time(args.start_hour, 0),
        end_time=time(args.end_hour, 0),
        times_per_hour=args.times_per_hour,
        days=args.days
    )

    screenshot.run()

if __name__ == '__main__':
    main()