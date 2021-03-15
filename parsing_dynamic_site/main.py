import json

import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 "
                      "Safari/537.36 "
    }

    # req = requests.get(url, headers=headers)
    #
    # with open("projects.html", "w") as file:
    #     file.write(req.text)

    with open("projects.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all("article", class_="ib19")

    projects_urls = []
    for article in articles:
        project_url = "http://www.edutainme.ru" + article.find("div", class_="txtBlock").find("a").get("href")

        projects_urls.append(project_url)

    projects_data_list = []
    for project_url in projects_urls:
        req = requests.get(project_url, headers)
        project_name = project_url.split("/")[-2]

        with open(f"data/{project_name}.html", "w") as file:
            file.write(req.text)

        with open(f"data/{project_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        project_data = soup.find("div", class_="inside")

        try:
            project_logo = "http://www.edutainme.ru" + project_data.find("div", class_="Img logo").find("img").get("src")
        except Exception:
            project_logo = "No project logo"

        try:
            project_name = project_data.find("div", class_="txt").find("h1").text
        except Exception:
            project_name = "No project name"

        try:
            project_short_description = project_data.find("div", class_="txt").find("h4", class_="head").text
        except Exception:
            project_short_description = "No project short description"

        try:
            project_website = project_data.find("div", class_="txt").find("p").find("a").text
        except Exception:
            project_website = "No project site"

        try:
            project_full_description = project_data.find("div", class_="textWrap").find("div", class_="rBlock").text
        except Exception:
            project_full_description = "No full description"

        projects_data_list.append(
            {
                "Имя проекта:": project_name,
                "URL логотипа проекта:": project_logo,
                "Короткое описание:": project_short_description,
                "Сайт проекта:": project_website,
                "Полное описание проекта:": project_full_description.strip()
            }
        )

    with open(f"data/projects_data.json", "a", encoding="utf-8") as file:
        json.dump(projects_data_list, file, indent=4, ensure_ascii=False)



get_data("http://www.edutainme.ru/edindex/")
