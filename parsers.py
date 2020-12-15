import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


url_podborka = 'https://www.filmpro.ru/materials/selections'

boevik = 22
multfilm = 21
drama = 6
sci_fi = 17
anime = 31
comedy = 3
vestern= 26

def get_selections():
    films = {}
    counter = 0
    main_url = 'https://filmpro.ru'
    r = requests.get(url_podborka)
    soup = BeautifulSoup(r.text, 'html.parser')
    filmsdata = soup.find_all(
        'div', attrs={'class': 'b-maincollections__itemwrapper'})
    for i in filmsdata:
        films_count = str(i).split('ount">')[1].split('</p')[0].strip()
        films_name = str(i).split('filmstitle">')[1].split('</p')[0].strip()
        films_link = main_url + \
            str(i).split('imagelink" href="')[1].split('">')[0].strip()
        films[counter] = {'films_count': films_count,
                          'films_name': films_name, 'films_link': films_link}
        counter += 1
    return films


def get_genre(genre):
    wbd_options = webdriver.ChromeOptions()
    wbd_options.add_argument('headless')
    webd = webdriver.Chrome(options=wbd_options, executable_path='C:/Users/Baytik-229/Загрузки/chromedriver_win32/chromedriver.exe')
    webd.get('https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]={}'.format(
        genre))
    time.sleep(10)
    a = webd.page_source
    # r = requests.get(url)
    soup = BeautifulSoup(a, 'html.parser')
    films = soup.find_all(
        'div', attrs={'class': 'b-maintopfilms__itemwrapper'})
    films_dict = {}
    counter = 0
    for i in films:
        film_name = str(i).split('img alt="')[1].split('"')[0].strip()
        film_link = 'https://filmpro.ru' + str(i).split('link" href="')[1].split('"')[0].strip()
        film_genre = str(i).split('genre">')[1].split('</p')[0].strip()
        films_dict[counter] = {'film_name': film_name,
                               'film_link': film_link, 'film_genre': film_genre}
        counter += 1
    return films_dict
