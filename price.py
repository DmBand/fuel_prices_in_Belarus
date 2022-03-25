from bs4 import BeautifulSoup
import requests
import datetime


def get_price(url):
    # print(response)
    soup = BeautifulSoup(url.text, 'html.parser')
    name = soup.select('.cert__title-txt')
    strong_all = soup.find_all('strong')
    rubles = [i.text for i in strong_all if i.text.isdigit()]
    kopecks = soup.find_all('sup')

    current_price = [f'{r},{k.text}' for r, k in zip(rubles, kopecks)]

    with open('price.txt', 'a', encoding='UTF-8') as file:
        file.write(f'\n{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n{"=" * 20}\n')
        for n, p in zip(name, current_price):
            file.write(f'{n.text}: {p}руб.\n')


def main():
    resource = requests.get("https://azs.a-100.by/set-azs/fuel/")
    get_price(resource)


if __name__ == '__main__':
    main()
