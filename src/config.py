# 取得対象URL
TARGET_URL = "https://news.yahoo.co.jp/"

# CSV出力ファイル名
CSV_OUTPUT_DIR = "output"
# logsファイル名
LOG_FILE_NAME = "logs/scraping.log"

# キーワード絞り込みを使うか
USE_KEYWORDS_FILTER = True

# 絞り込み対象キーワード
KEYWORDS = ["AI", "Python", "IT"]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

DB_FILE_NAME = "output/news.db"