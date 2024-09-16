import os
import subprocess
import datetime

# 日付を使用してファイルに変更を加える
def make_commit():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("commit.txt", "a") as file:
        file.write(f"Commit on {today}\n")

    # Gitのステージングとコミット
    subprocess.run(["git", "add", "commit.txt"])
    subprocess.run(["git", "commit", "-m", f"Commit on {today}"])
    subprocess.run(["git", "push"])

# 毎日コミットする
make_commit()
