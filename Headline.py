import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for h in soup.find_all("h2"):
    text = h.get_text(strip=True)
    if text:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, headline in enumerate(headlines, 1):
        f.write(f"{i}. {headline}\n")

print(f"Scraped {len(headlines)} headlines and saved to 'headlines.txt'")
