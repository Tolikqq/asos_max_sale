from bs4 import BeautifulSoup
import requests

def parse_asos(url):
    nextPage = True
    new_news = []
    news = []

    while nextPage:
        page = getPage(url)
        soup = BeautifulSoup(page.text, "lxml")

        news = soup.findAll('a', class_='_3TqU78D')
        for i in range(len(news)):
            if news[i].find('span', class_='_16nzq18') is not None:
                try:
                    price = news[i].find('span', {'class': '_16nzq18'}).text
                    price_sale = news[i].find('span', {'class': '_22sbBtS'}).text

                    price = float(price.replace('руб.', '').replace(',', '.').replace(' ', ''))
                    price_sale = float(
                        price_sale.replace('руб.', '').replace(',', '.').replace(' ', ''))

                    dictionary = {
                        'name': news[i].text,
                        'url': news[i].get('href'),
                        'price': price,
                        'price_sale': price_sale,
                        'sale': int((price_sale / price - 1) * 100)
                    }
                    new_news.append(dictionary)
                except:
                    print("mistake")
                    continue
        if soup.find(rel="next") is not None:
            url = str(soup.find(rel="next").get('href'))
        else:
            nextPage = False

    return new_news


def getPage(url):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    return session.get(url, verify=False)
