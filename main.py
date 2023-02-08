import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import pandas as pd

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()


response=requests.get('https://spb.hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true', headers=get_headers())
habr_main = response.text

soup = BeautifulSoup(habr_main, 'lxml')

# website =soup.find('a', class_='serp-item__title').get('href')
# print(website)
#
# company = soup.find('a', class_='bloko-link bloko-link_kind-tertiary').text
# print(company)
#
# city = soup.find('div', class_='bloko-text').text
# print(city)
#
# salery = soup.find('span', class_='bloko-header-section-3').text
# print(salery)

vacances = soup.findAll('div', class_='serp-item')
# print(len(vacances))

data = []

for vacancy in vacances:
    website = vacancy.find('a', class_='serp-item__title').get('href')
    company = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary').text
    city = vacancy.find('div', class_='bloko-text').text
    try:
        salery = vacancy.find('span', class_='bloko-header-section-3').text
    except:
        salery = '-'
    data.append([website, company, city, salery])

print(data)

header = ['website', 'company', 'city', 'salery']

df = pd.DataFrame(data, columns=header)
df.to_csv('/Users/desktop/vacance.csv', sep=';', encoding='utf8')
