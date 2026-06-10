from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def get_html_user_films(name: str, page_number: int,**kwargs):
    url = f'https://letterboxd.com/{name}/diary/films/page/{page_number}/'
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(10)

    resp = driver.page_source

    if "Letterboxd - Not Found" in resp:

        driver.quit()

        return "Usuario não encontrado"

    else:

        resp = driver.page_source

        driver.quit()

        return resp

def get_html_film(name: str, **kwargs):
    url = f'https://letterboxd.com/film/{name}/' 
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)

    driver.get(url)
    time.sleep(10)

    resp = driver.page_source

    if "Letterboxd - Not Found" in resp:
        driver.quit()

        return "Usuario não encontrado"

    else:
        resp = driver.page_source

        driver.quit()
        return resp
