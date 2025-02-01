from serpapi import GoogleSearch

params = {
  "engine": "google",
  "q": "查找一下今天的金融新闻",
  "api_key": "cdc3b207606843b4c883849c3a0f833c13057811bea964bef192707d8845f3d8"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(organic_results)
#
# print(organic_results[0]['snippet'])
#
# import requests
# from bs4 import BeautifulSoup
#
# # 目标网站的URL
# url = "https://www.aibase.com/zh/news"  # 替换为你要爬取的网站
#
# # 发送HTTP GET请求
# response = requests.get(url)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 解析HTML内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 提取所有文本内容
#     all_text = soup.get_text(separator='\n')  # 用换行符分隔文本
#
#     # 打印所有内容
#     print(all_text)
#
#     # 如果需要保存到文件
#     with open('website_content.txt', 'w', encoding='utf-8') as file:
#         file.write(soup)
# else:
#     print(f"Failed to retrieve the website. Status code: {response.status_code}")


