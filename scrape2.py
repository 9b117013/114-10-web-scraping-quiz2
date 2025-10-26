import requests
from bs4 import BeautifulSoup
import json

def main():
    url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            # 建立 BeautifulSoup 物件，使用 lxml 解析器
            soup = BeautifulSoup(response.text, 'lxml')
            books = []
            # 找出所有書籍容器
            articles = soup.find_all('article', class_='product_pod')
            
            for article in articles:
                # 擷取書名：從 h3 > a 標籤的 title 屬性
                h3_tag = article.find('h3')
                if h3_tag:
                    a_tag = h3_tag.find('a')
                    if a_tag:
                        title = a_tag.get('title')
                    else:
                        title = None
                else:
                    title = None
                
                # 擷取價格
                price_tag = article.find('p', class_='price_color')
                if price_tag:
                    price = price_tag.text
                else:
                    price = None
                
                # 擷取評分：從 class 屬性的第二個值
                rating_tag = article.find('p', class_='star-rating')
                if rating_tag:
                    classes = rating_tag.get('class')
                    if classes and len(classes) >= 2:
                        rating = classes[1]  # 第二個值是評分文字 (One, Two, Three...)
                    else:
                        rating = None
                else:
                    rating = None
                
                book = {
                    "title": title,
                    "price": price,
                    "rating": rating
                }
                
                books.append(book)
            
            # 輸出 JSON ，保留中文字元
            print(json.dumps(books, ensure_ascii=False, indent=2))
            
        else:
            print(f"請求失敗，狀態碼：{response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"發生錯誤：{e}")
    except Exception as e:
        print(f"解析錯誤：{e}")

if __name__ == "__main__":
    main()
