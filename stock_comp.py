from bs4 import BeautifulSoup
import requests


def get_competitors(ticker, exchange):
    try:
        response = requests.get(f"https://www.marketbeat.com/stocks/{exchange}/{ticker}/competitors-and-alternatives/", timeout=4)
    except Exception as msg:
        raise BaseException(f"{msg}")
    else:
        to_parse = response.text

        soup = BeautifulSoup(to_parse, "html.parser")
        competitors_html = soup.find_all(class_="ticker-area")

        competitors = []

        for comp in competitors_html:
            competitors.append(comp.getText())

        return competitors
