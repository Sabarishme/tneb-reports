import requests
import datetime
import os
import subprocess

os.makedirs("pdfs", exist_ok=True)

today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"pdfs/peakdet_{today}.pdf"

if os.path.exists(filename):
    print(f"Already exists: {filename}")
    exit()

url = "https://tnebsldc.org/reports1/peakdet.pdf"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code == 200 and len(response.content) > 1000:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Saved: {filename}")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"report {today}"])
        subprocess.run(["git", "push"])
        print("Pushed to GitHub!")
    else:
        print(f"Failed: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
