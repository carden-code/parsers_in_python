import requests
from bs4 import BeautifulSoup
import lxml
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 "
                  "Safari/537.36 "
}
# Список всех ссылок фестевалей.
fests_urls_list = []

for i in range(0, 24, 24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=17%20Mar%202021&to_date" \
          f"=&genre%5B%5D=pop&maxprice=500&o={i}&bannertitle=July"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w") as file:
        file.write(html_response)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all("a", class_="card-details-link")

    for item in cards:
        fest_url = "https://www.skiddle.com" + item.get('href')
        fests_urls_list.append(fest_url)

for url in fests_urls_list:
    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_info_block = soup.find("div", class_="top-info-cont")
        fest_name = fest_info_block.find("h1").text.strip()
    except Exception as ex:
        print(ex)
