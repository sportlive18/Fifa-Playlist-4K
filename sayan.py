import urllib.request
import os

# Example of using a secret from environment variables
# In GitHub Actions, this would be passed from secrets.MY_SECRET
my_secret = os.getenv("MY_SECRET", "no_secret_found")
print(f"Using secret: {my_secret[:3]}***")

url = "https://rkdyiptv.pages.dev/Playlist/Global.m3u"

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")

    with open("Sayan.m3u", "w", encoding="utf-8") as f:
        f.write(content)

    print("Saved as Sayan.m3u")
except Exception as e:
    print(f"Error: {e}")