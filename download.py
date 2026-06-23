import requests
import datetime
import os

# Create pdfs folder if not exists
os.makedirs("pdfs", exist_ok=True)

# Today's date
today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"pdfs/peakdet_{today}.pdf"

# Skip if already downloaded today
if os.path.exists(filename):
    print(f"Already exists: {filename}")
    exit()

# Download from TNEB
url = "https://tnebsldc.org/reports1/peakdet.pdf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    if response.status_code == 200 and len(response.content) > 1000:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved: {filename}")
    else:
        print(f"❌ Failed — Status: {response.status_code}, Size: {len(response.content)} bytes")
        exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
