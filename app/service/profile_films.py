# %%
from bs4 import BeautifulSoup
from html_letterboxd import get_html_user_films

def extraction_movies_tags(html: str, name: str):

    soup = BeautifulSoup(html,'html.parser')

    try:

        tags_info_profile_movie = soup.find_all('tr',{'data-owner': name})
        
        return tags_info_profile_movie

    except Exception as e:

        print(f'Ocorreu o seguinte erro durante a extração das tags: {e}')

        return None

name = 'yama21'
page = 1

html = get_html_user_films(name,page)
html
# %%
