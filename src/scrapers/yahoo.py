import requests
from bs4 import BeautifulSoup

from config import HEADERS


def fetch_yahoo_news():
    url = "https://news.yahoo.co.jp/"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    seen_urls = set()

    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")

        if not title or not href:
            continue

        if "news.yahoo.co.jp/articles/" not in href:
            continue

        if href in seen_urls:
            continue

        seen_urls.add(href)

        articles.append({
            "title": title,
            "url": href,
            "source": "Yahoo!ニュース",
        })

    return articles