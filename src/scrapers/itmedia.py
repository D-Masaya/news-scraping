import requests
from bs4 import BeautifulSoup


def fetch_itmedia_news():
    url = "https://www.itmedia.co.jp/news/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # 文字化け対策
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    seen_urls = set()

    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")

        if not title or not href:
            continue

        if "/news/articles/" not in href:
            continue

        if href.startswith("/"):
            href = "https://www.itmedia.co.jp" + href

        if href in seen_urls:
            continue

        seen_urls.add(href)

        articles.append({
            "title": title,
            "url": href,
            "source": "ITmedia NEWS",
        })

    return articles