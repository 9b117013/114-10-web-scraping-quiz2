import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "https://www.books.com.tw/web/sys_saletopb/books/19?attribute=30"
    
    # 設定 User-Agent 模擬瀏覽器，避免被網站封鎖
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            books = []
            items = soup.find_all('div', class_='type02_bd-a')
            
            # enumerate 從 1 開始，取前 20 筆
            for idx, item in enumerate(items[:20], 1):
                # 擷取書名
                h4_tag = item.find('h4')
                if h4_tag:
                    a_tag = h4_tag.find('a')
                    if a_tag:
                        title = a_tag.text.strip()
                    else:
                        title = None
                else:
                    title = None
                
                # 擷取價格：從第二個 strong 標籤中的 b 標籤
                price_li = item.find('li', class_='price_a')
                if price_li:
                    strong_tags = price_li.find_all('strong')
                    if len(strong_tags) >= 2:
                        b_tag = strong_tags[1].find('b')  # 第一個是折扣，第二個是價格
                        if b_tag:
                            price = "NT$" + b_tag.text.strip()
                        else:
                            price = None
                    else:
                        price = None
                else:
                    price = None
                
                rank = str(idx)
                
                book = {
                    "title": title,
                    "price": price,
                    "rank": rank
                }
                
                books.append(book)
            
            # 輸出 JSON 格式，保留中文字元
            print(json.dumps(books, ensure_ascii=False, indent=2))
            
        else:
            print(f"請求失敗，狀態碼：{response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"發生網路錯誤：{e}")
    except Exception as e:
        print(f"解析錯誤：{e}")

if __name__ == "__main__":
    main()
