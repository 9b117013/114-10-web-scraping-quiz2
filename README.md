# 線上圖書銷售網站爬蟲

## 功能說明

### scrape1.py
- 使用 requests 和正規表示式 (RE) 從 Books to Scrape 網站爬取旅遊類書籍的價格
- 輸出所有價格的列表

### scrape2.py
- 使用 requests 和 BeautifulSoup4 從 Books to Scrape 網站爬取旅遊類書籍的完整資訊
- 包含：書名、價格、評分
- 輸出 JSON 格式

### scrape3.py
- 使用 requests 和 BeautifulSoup4 從博客來網站爬取電腦資訊類30日排行榜前20名
- 包含：書名、價格、排名
- 輸出 JSON 格式

## 安裝說明
```bash
pip install -r requirements.txt
```

## 執行方式
```bash
python scrape1.py
python scrape2.py
python scrape3.py
```

## 使用技術
- Python 3
- requests - HTTP 請求
- BeautifulSoup4 - HTML 解析
- lxml - 解析器
- re - 正規表示式

## 專案結構
```
web-scraping-quiz2/
├── scrape1.py          
├── scrape2.py          
├── scrape3.py          
├── requirements.txt    
├── .gitignore         
├── LICENSE            
└── README.md          
```

## 注意事項
- 程式包含錯誤處理機制
- 檢查 HTTP 狀態碼確保請求成功

## 作者
9b117013