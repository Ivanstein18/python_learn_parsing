import requests
from bs4 import BeautifulSoup

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

with open("index.html") as file:
    src = file.read()
    
soup = BeautifulSoup(src, "lxml")
all_products_href = soup.find_all(class_ = "mzr-tc-group-item-href")
for item in all_products_href:
    item_text = item.text
    item_href = item.get("href")
    print(f"{item_text}:{item_href}")

