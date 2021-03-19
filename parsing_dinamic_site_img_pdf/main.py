import os

import requests
import img2pdf


def get_data():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                  "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/89.0.4389.82 Safari/537.36"
    }

    img_list = []
    # Обход всех страниц, получение изображений.
    for i in range(1, 49):
        url = f"http://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        # Запись контента(Изображений) в файл в двоичном виде.
        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Downloaded {i} of 48")
    print("#" * 20)
    print(img_list)

    # Конвертация в PDF
    with open("result.pdf", "wb") as file:
        file.write(img2pdf.convert(img_list))

    print("PDF file created successfully")


# # # Если изображения уже скачены.
# def write_to_pdf():
#     print(os.listdir("media"))
#     img_list = [f"media/{i}.jpg" for i in range(1, 49)]
#
#     # Create PDF file
#     with open("result.pdf", "wb") as file:
#         file.write(img2pdf.convert(img_list))
#     print("PDF file created successfully")


def main():
    get_data()
    # write_to_pdf()


if __name__ == '__main__':
    main()
