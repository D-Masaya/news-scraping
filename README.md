# News Scraping Tool

Yahoo!ニュース / ITmedia NEWS からニュース記事情報を取得し、CSVファイルへ出力するPython製スクレイピングツールです。

## 概要

このツールでは、複数ニュースサイトから記事タイトル・URLを取得し、CSVとして保存できます。  
キーワードによる絞り込み、重複除外、ログ出力、サイト別CSV出力にも対応しています。

## 主な機能

- Yahoo!ニュースの記事取得
- ITmedia NEWSの記事取得
- 記事タイトル取得
- 記事URL取得
- ニュース提供元の記録
- 重複URLの除外
- キーワード絞り込み
- 取得日時の記録
- 全件CSV出力
- サイト別CSV出力
- ログ出力
- エラー処理
- 設定ファイル分離

## 使用技術

- Python
- requests
- BeautifulSoup4
- csv
- logging

## ディレクトリ構成

```text
news_scraping/
├─ src/
│  ├─ main.py
│  ├─ config.py
│  └─ scrapers/
│     ├─ yahoo.py
│     └─ itmedia.py
├─ output/
├─ logs/
├─ run.bat
├─ requirements.txt
├─ .gitignore
└─ README.md