import requests
import pandas as pd
from bs4 import BeautifulSoup

url0 = 'https://kissmanga.in/kissmanga/solo-leveling-manhwa-read/chapter-198/'


def run(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_list = soup.find_all('img', class_="wp-manga-chapter-img")

    img_urls = []
    for img in img_list:
        a = (img.get('src').split())
        img_urls.extend(a)

    c = 0
    for img_url in img_urls:
        c += 1
        image = requests.get(img_url)
        image_title = url.split('/')[-2]+f'-{c}.jpg'
        with open(image_title, 'wb') as file:
            file.write(image.content)

    if {soup.find('a', {'class': 'next_page'})} == None:
        print('done')
        return

    else:
        next_page_link = soup.find('a', {'class': 'next_page'})['href']
        url = next_page_link
        run(url)


if __name__ == '__main__':
    run(url0)
