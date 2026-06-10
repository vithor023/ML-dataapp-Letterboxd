# %%
from bs4 import BeautifulSoup
from html_letterboxd import get_html_user_films

def extraction_movies_tags(html: str, name: str):

    soup = BeautifulSoup(html,'html.parser')

    try:

        tags_info_profile_movie = soup.find_all('tr',{'data-owner': name})
        
        return tags_info_profile_movie

    except Exception as e:

        msg = str(e)
        erro = {'Tags extraidas': None,'erro': e }
        return erro

def extraction_number_pages_movie(html: str, name: str):

    soup = BeautifulSoup(html,'html.parser')
    try:

        tag_number_page = soup.find_all('li',class_='paginate-page')
        number_pages  = int(tag_number_page[-1].a.text)
        return number_pages
    
    except Exception as e:
        msg = str(e)
        erro = {'Tags extraidas': None,'erro': e }
        return erro


