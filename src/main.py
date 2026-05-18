import csv
import logging
import os
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from config import (
    TARGET_URL,
    CSV_OUTPUT_DIR,
    LOG_FILE_NAME,
    USE_KEYWORDS_FILTER,
    KEYWORDS,
)

os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_NAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

def fetch_news():
    articles = []
    seen_urls = set()
    scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = requests.get(TARGET_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")

        if not title or not href:
            continue

        if "news.yahoo.co.jp/articles/" not in href:
            continue

        if href in seen_urls:
            continue

        if USE_KEYWORDS_FILTER and not any(keyword in title for keyword in KEYWORDS):
            continue

        seen_urls.add(href)

        articles.append({
            "title": title,
            "url": href,
            "scraped_at": scraped_at,
        })

    return articles


def save_to_csv(articles, csv_file_name):
    with open(csv_file_name, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "url", "scraped_at"])
        writer.writeheader()
        writer.writerows(articles)


def main():
    try:
        logging.info("ニュース取得処理を開始しました。")

        articles = fetch_news()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file_name = f"{CSV_OUTPUT_DIR}/news_{timestamp}.csv"

        save_to_csv(articles, csv_file_name)

        if len(articles) == 0:
            logging.warning("該当するニュースが0件でした。")
            print("該当するニュースが0件でした。")
        else:
            logging.info(f"CSV保存が完了しました：{len(articles)}件")
            print(f"CSV保存が完了しました：{len(articles)}件")
            print(f"保存先: {csv_file_name}")

    except requests.exceptions.RequestException as e:
        logging.error(f"通信エラーが発生しました：{e}")
        print("通信エラーが発生しました。ログを確認してください。")

    except Exception as e:
        logging.exception(f"予期しないエラーが発生しました：{e}")
        print("予期しないエラーが発生しました。ログを確認してください。")


if __name__ == "__main__":
    main()