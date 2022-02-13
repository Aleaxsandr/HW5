import requests
from  bs4 import BeautifulSoup
from  time import  sleep
import  pandas as pd

url = 'https://www.kinopoisk.ru/lists/top250/'
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
soup.find('div', class_='desktop-rating-selection-film-item')
soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link')
link = 'https://www.kinopoisk.ru'+soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').get('href')
print(link)
russian_name = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
print(russian_name)
original_name = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
print(original_name)
country_name = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
print(country_name)
film_type = soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
print(film_type)
film_reting = soup.find('div', class_='desktop-rating-selection-film-item').find('span', class_='rating__value rating__value_positive').text
print(film_reting)
data = []
for p in range(1, 6):
    print(p)
    url = f'https://www.kinopoisk.ru/lists/top250/?page={p}&tab=all'
    r = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div',class_='desktop-rating-selection-film-item' )



    for film in films:
        link = 'https://www.kinopoisk.ru'+film.find('a', class_='selection-film-item-meta__link').get('href')
        russian_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
        original_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
        country_name = film.find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
        film_type = film.find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
        film_reting = film.find('span', class_='rating__value rating__value_positive').text

        data.append([link, russian_name, original_name, country_name, film_type, film_reting])
len(data)
header = ['link', 'russian_name', 'original_name', 'country_name', 'film_type', 'film_reting']
df = pd.DataFrame(data, columns=header)
df.to_csv('kinopoisk_data.csv', sep=';', encoding='utf8')

