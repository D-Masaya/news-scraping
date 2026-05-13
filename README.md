# News Scraping Tool

Yahoo!ニュースから記事タイトルとURLを取得し、CSVファイルに出力するPythonツールです。

## 機能

- ニュース記事のタイトル取得
- 記事URLの取得
- 重複URLの除外
- キーワードによる絞り込み
- CSV出力
- ログ出力
- エラー処理

## 使用技術

- Python
- requests
- BeautifulSoup

## セットアップ

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt