# %%
import requests

def get_html_user_films(name: str):

    resp = requests.get(f'https://letterboxd.com/{name}/diary/')

    if resp.status_code != 200:
        return "Usuario não ecnontrado"
    else:
        return resp.text

html = get_html_user_films('yama21')
html