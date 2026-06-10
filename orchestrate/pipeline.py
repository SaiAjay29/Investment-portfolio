import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
import schedule
import time

from extract.fetch_data import fetch_all_assets
from transform.clean_transform import run_transform
from load.load_to_db import run_load

def run_pipeline():
    print(f"\n{'='*50}")
    print(f"Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    try:
        print("Step 1: Extract")
        fetch_all_assets()

        print("Step 2: Transform")
        run_transform()

        print("Step 3: Load")
        run_load()

        print(f"Pipeline completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"Pipeline failed: {e}")

def start_scheduler():
    # Run every day at 7am
    schedule.every().day.at("07:00").do(run_pipeline)

    print("Scheduler started. Pipeline runs daily at 7am.")
    print("Press Ctrl+C to stop.\n")

    # Run once immediately on start
    run_pipeline()

    if __name__ == "__main__":
    run_pipeline())

if __name__ == "__main__":
    start_scheduler()
