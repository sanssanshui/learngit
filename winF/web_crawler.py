import requests
from bs4 import BeautifulSoup
import time
import random

#爬取网站的文本
def main():
    url = "https://baike.baidu.com/item/Python/407313"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xe28077b700103d6d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=40020637_19_oem_dg&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100&rsv_btype=i&prefixsug=python&rsp=3&inputT=733&rsv_sug4=733",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    time.sleep(random.uniform(1, 3))

    try:
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")

        content_div = soup.find("div", class_ = "main-content")
        paragraphs = []
        if content_div:
            for p in content_div.find_all("p"):
                if p.text.strip():
                    paragraphs.append(p.text.strip())
            article_text = "\n\n".join(paragraphs)
        else:
            article_text = "获取失败"

        with open("test.txt", "w", encoding = "utf-8") as f:
            f.write("\n".join(paragraphs))
            f.write("\n\n" + article_text)
        
        print("内容保存成功")
    except Exception as e:
        print(f"抓取失败：{str(e)}")

if __name__ == "__main__":
    main()