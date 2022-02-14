import selenium
from  bs4 import BeautifulSoup
from  time import  sleep
import  pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

header = {
    #Сюда помещаем наш user-agent
    'User_Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'}
driver = webdriver.Chrome(executable_path='C:\\Users\\ADMIN\\Desktop\\chromedriver\\chromedriver_win32\\chromedriver.exe')
url = 'https://www.kinopoisk.ru/lists/top250/'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
print(soup)
soup.find('div', class_='desktop-rating-selection-film-item')\
    .find('a', class_='selection-film-item-meta__link')
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
    driver.get(url)
    html = driver.page_source
    sleep(3)
    soup = BeautifulSoup(html, 'lxml')

    films = soup.findAll('div',class_='desktop-rating-selection-film-item' )

    for film in films:
        link = 'https://www.kinopoisk.ru'+film.find('a', class_='selection-film-item-meta__link').get('href')
        russian_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
        original_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
        country_name = film.find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
        film_type = film.find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__meta-additional-item')[1].text
        try:
            film_reting = film.find('span', class_='rating__value rating__value_positive').text
        except:
            film_reting = '-'

        data.append([link, russian_name, original_name, country_name, film_type, film_reting])
len(data)
header = ['link', 'russian_name', 'original_name', 'country_name', 'film_type', 'film_reting']

df = pd.DataFrame(data, columns=header)
df.to_csv('kinopoisk_data.csv', sep=';', encoding='utf8')




