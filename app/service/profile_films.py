from datetime import datetime
from bs4 import BeautifulSoup

def extraction_movies_tags(html: str, name: str) -> list:

    soup = BeautifulSoup(html,'html.parser')

    try:

        tags_info_profile_movie = soup.find_all('tr',{'data-owner': name})
        
        return tags_info_profile_movie

    except Exception as e:

        msg = str(e)
        erro = {'Tags extraidas': None,'erro': e }
        return erro

def extraction_number_pages_movie(html: str, name: str) -> int:

    soup = BeautifulSoup(html,'html.parser')
    try:

        tag_number_page = soup.find_all('li',class_='paginate-page')
        number_pages  = int(tag_number_page[-1].a.text)
        return number_pages
    
    except Exception as e:
        msg = str(e)
        erro = {'Tags extraidas': None,'erro': e }
        return erro

def clear_movie_profile(lista_tag: list) -> list:
    
    list_movie = []

    for row in lista_tag:

        row_movie_rate = row.find('div',class_='rating-green').find('span').get('class')
        row_movie_like = row.find('td',class_='col-like -align-center -padding-inline-large')

        movie_obj = {}
        movie_obj['data_watched'] = row.find('a',class_='daydate').get('href').split('for/')[-1].rstrip('/')
        movie_obj['movie_name'] = row.find('div',class_='react-component figure').get('data-item-name')
        movie_obj['year_released'] = int(movie_obj['movie_name'].split('(')[-1].rstrip(')'))
        movie_obj['nota'] = int(row_movie_rate[-1].split('-')[-1]) if len(row_movie_rate) == 2 else 0
        movie_obj['is_liked'] = 1 if row_movie_like.find('span',class_='has-icon icon-16 icon-liked hide-for-owner') else 0
        movie_obj['is_rewatch'] = 0 if row.find('td',class_='col-rewatch -align-center -padding-inline-large js-td-rewatch icon-status-off') else 1
        movie_obj['is_rewiewd'] = 1 if row.find('td',class_='col-review -align-center -padding-inline-large js-td-review') else 0
        list_movie.append(movie_obj)

    return list_movie

def movie_sluged_for_link_movie(lista_tag: list) -> list:
    
    list_sluged_movie = [row.find('div',class_='react-component figure').get('data-item-slug') 
                        for row in lista_tag]
    
    return list_sluged_movie

