# News Scraping Tool

Yahoo!ニュースから記事情報を取得し、
CSVへ出力するPython製スクレイピングツールです。

## 機能

- ニュースタイトル取得
- URL取得
- 重複除外
- キーワード絞り込み
- CSV出力
- ログ出力
- エラー処理
- 設定ファイル分離
- 日付付きCSV出力

## 使用技術

- Python
- requests
- BeautifulSoup4

## ディレクトリ構成

```text
news_scraping/
├─ src/
├─ output/
├─ logs/
├─ run.bat
├─ requirements.txt
└─ README.md