from bs4 import BeautifulSoup
import requests
#


def parse_a_website(url) -> BeautifulSoup:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    return soup
