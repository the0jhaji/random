import os
import random
import subprocess
from datetime import datetime, timedelta


start_date = datetime(2024, 8,18)
end_date = datetime(2026, 9,25)

current_date = start_date

while current_date <= end_date:  
    num_commits = random.randint(0, 2)

    for i in range(num_commits):
        # Random time during the day
        commit_time = current_date.replace(
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )

        date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        # Modify a file so Git detects a change
        with open("activity.txt", "a", encoding="utf-8") as f:
            f.write(f"Commit on {date_str}\n")

        subprocess.run(["git", "add", "."])

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        subprocess.run(
            ["git", "commit", "-m", f"Update {date_str}"],
            env=env
        )

    current_date += timedelta(days=1)

# Push all commits
subprocess.run(["git", "push", "origin", "master"])