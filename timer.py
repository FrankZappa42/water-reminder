import argparse
import time
import os

def display_notification(message):
    # Construct the command to display a macOS notification
    command = f"osascript -e 'display notification \"{message}\" with title \"Drink Water\"'"
    os.system(command)

def main():
    parser = argparse.ArgumentParser(description="30-Minute Timer")
    parser.add_argument("duration", type=int, help="Duration in minutes")
    args = parser.parse_args()
    duration = args.duration

    total_seconds = duration * 60

    while total_seconds > 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        if minutes % 30 == 0 and seconds == 0:
            display_notification("Drink water!")  # Display notification every 30 minutes

        print(f"Time remaining: {minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up!")

if __name__ == "__main__":
    main()
