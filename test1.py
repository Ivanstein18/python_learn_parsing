import requests
from bs4 import BeautifulSoup
import json

# url = "http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# headers = {
# "Accept": "*/*",
# "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
# }

# req = requests.get(url, headers=headers)

# src = req.text
# # print(src)

# with open("index.html", "w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
    
# soup = BeautifulSoup(src, "lxml")
# all_products_href = soup.find_all(class_ = "mzr-tc-group-item-href")

# all_categories_dict = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = "http://health-diet.ru" + item.get("href")
    
#     all_categories_dict[item_text] = item_href

# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

print(all_categories)

