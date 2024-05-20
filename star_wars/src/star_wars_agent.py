import json
import requests
from . import star_wars_config as config
from . import star_wars_endpoint as endpoints

requests.packages.urllib3.disable_warnings()

class StarWarAgent():
    def __init__(self):
        self.headers = {            
            'accept': 'text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://swapi.dev/',
            'x-requested-with': 'XMLHttpRequest'
        }

    def get_request(self, url, headers):
        print("GET - "+url)
        return requests.get(url, headers, verify=False)

    def post_request(self, url, headers, payload):
        print("POST - "+url)
        data = json.dumps(payload)
        return requests.post(url, headers, data=data, verify=False)
    
    def get_all_films(self):
        url = config.url + endpoints.film
        return self.get_request(url,self.headers)
    
    def get_film_by_id(self, idNumber=""):
        url = config.url + endpoints.filmById.format(idNumber=idNumber)
        return self.get_request(url,self.headers)
    
    def get_people(self, idNumber=""):
        url = config.url + endpoints.people.format(idNumber=idNumber)
        return self.get_request(url,self.headers)
    
    def get_planet(self, idNumber=""):
        url = config.url + endpoints.planets.format(idNumber=idNumber)
        return self.get_request(url,self.headers)