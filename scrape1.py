import requests
import re

def main():
    url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            html = response.text
            # 正規表示式：£ + 數字 + . + 兩位數字
            pattern = r'£\d+\.\d{2}'
            # 找出所有符合價格格式的字串
            prices = re.findall(pattern, html)
            print(prices)
        else:
            print(f"請求失敗，狀態碼：{response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    main()
