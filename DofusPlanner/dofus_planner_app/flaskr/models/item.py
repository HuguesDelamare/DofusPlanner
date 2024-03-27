import requests
from db import get_db

class Item:
    @staticmethod
    def fetch_from_api(name):
        api_url = f'https://api.beta.dofusdb.fr/items?name.fr{name}'
        response = requests.get(api_url)

        if response.ok:
            return response.json().get('data')
        else:
            return None
        
    @staticmethod
    def process_data(data):
        pass