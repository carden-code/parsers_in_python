import requests
from bs4 import BeautifulSoup
import json

# url = "https://health-diet.ru/table_calorie/"
#
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 "
                  "Safari/537.36 "
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
#
# all_categories_dict = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get('href')
#
#     all_categories_dict[item_text] = item_href
#     # print(f'{item_text}: {item_href}')
#
# # Запись словаря в json файл.
# # indent - отступы. ensure_ascii - не экранирует символы, помогает при работе с кирилицей.
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# Загрузим файл json в переменную.
with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

count = 1
for category_name, category_href in all_categories.items():

    if count == 1:
        rep = [",", " ", "-", "'"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, '_')

        req = requests.get(url=category_href, headers=headers)
        src = req.text

        with open(f"data/{count}_{category_name}.html", "w") as file:
            file.write(src)

        with open(f"data/{count}_{category_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        # Собираем заголовки таблицы
        table_head = soup.find(calss_="mzr-tc-group-table")
        print(table_head)

        count += 1
