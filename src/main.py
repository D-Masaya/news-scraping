import csv
import logging
import os
from datetime import datetime

import requests

from config import (
    CSV_OUTPUT_DIR,
    LOG_FILE_NAME,
    USE_KEYWORDS_FILTER,
    KEYWORDS,
    DB_FILE_NAME,
)

from scrapers.yahoo import fetch_yahoo_news
from scrapers.itmedia import fetch_itmedia_news
from db import initialize_db, save_to_db


os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_NAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)


def filter_articles_by_keywords(articles):
    if not USE_KEYWORDS_FILTER:
        return articles

    return [
        article for article in articles
        if any(keyword in article["title"] for keyword in KEYWORDS)
    ]


def save_to_csv(articles, csv_file_name):
    with open(csv_file_name, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "url", "source", "scraped_at"]
        )
        writer.writeheader()
        writer.writerows(articles)

def save_csv_by_source(articles, timestamp):
    articles_by_source = {}

    for article in articles:
        source = article["source"]
        articles_by_source.setdefault(source, []).append(article)

    for source, source_articles in articles_by_source.items():
        if source == "Yahoo!ニュース":
            file_name = f"{CSV_OUTPUT_DIR}/yahoo_news_{timestamp}.csv"
        elif source == "ITmedia NEWS":
            file_name = f"{CSV_OUTPUT_DIR}/itmedia_news_{timestamp}.csv"
        else:
            file_name = f"{CSV_OUTPUT_DIR}/news_{timestamp}.csv"

        save_to_csv(source_articles, file_name)


def main():
    try:
        logging.info("ニュース取得処理を開始しました。")

        scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file_name = f"{CSV_OUTPUT_DIR}/all_news_{timestamp}.csv"

        articles = []

        articles.extend(fetch_yahoo_news())
        articles.extend(fetch_itmedia_news())

        articles = filter_articles_by_keywords(articles)

        for article in articles:
            article["scraped_at"] = scraped_at

        save_to_csv(articles, csv_file_name)
        save_csv_by_source(articles, timestamp)
        
        initialize_db(DB_FILE_NAME)
        save_to_db(articles, DB_FILE_NAME)

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