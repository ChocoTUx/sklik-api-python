from abc import ABC, abstractmethod
from xmlrpc import client
from requests import post
from datetime import datetime
import ssl
import json
import src.xmlrpc_client_monkeypatch

class Root():
        '''
        Central class for all common things about requests
        Work with config and do login
        '''

        def __init__(self, type='xml', token='default'):
                '''
                Setup all things what user need for use Sklik API
                '''
                self.type = type
                self.token = token                
                self.load_config()
                if type is 'json':
                        self.url = self.config['url']['json']
                        self.api = JsonApi(self.url)
                else:
                        self.url = self.config['url']['xml']
                        self.api = XmlApi(self.url)
                self.login_in_by_token()

        def load_config(self):
                '''
                Load config file where are information about account    
                '''
                with open('./../src/conf_local.json') as f:
                        self.config = json.load(f)

        def get_token(self)-> str:
                return self.config['token'][str(self.token)]

        def get_url(self, type)-> str:
                return self.url

        def get_api(self):
                return self.api

        def get_logged_user_struct(self, user)-> object:
                '''
                Api requests need stuct user (session and user ID) as a fist param of query
                '''
                return {'session': self.api.get_session(), 'userId': self.config['users'][str(user)]}

        def login_in_by_token(self):
                '''
                Before other question user need do authentication and get session
                '''
                self.api.login_by_token(self.get_token())

        def logout(self):
                '''
                When all stuff are done, do logout (teardown session)
                '''
                self.api.logout()


class Api(ABC):
        '''
        Trida urcena pro praci s Sklik API. 
        Zastresuje vsechny akce, pro ktere neni treba rozlisovat typ spojeni
        '''
        
        def __init__(self, url):
                self.url = url

        def login_by_token(self, token)-> str:
                '''
                Prihlasovani bude probihat pomoci JSON (bez ohledu na to, jestli pak budeme testovat XML volani)
                Samotny test prihlasovani probehne jako klasicky test na zacatku testovani
                :raises:
                        Exception: Pokud se nepodari prihlasit (session nevraci 200)
                '''
                response = self.call('client.loginByToken', token)
                if response["status"] == 200:
                        self.session = response["session"]
                        return self.session
                else:
                        raise Exception('Nelze se přihlásit')

        def get_session(self)-> str:
                return self.session
                        
        def logout(self)-> bool:
                '''
                Logout actual client and teardown session
                '''
                response = self.call('client.logout',{'session': self.session})
                if response["status"] != 200:
                        raise Exception('Nelze se odhlásit')

        def date_trans(self, date, type):
                '''
                Format for json: 2019-01-22
                '''
                date = datetime.strptime(date, "%d.%m.%Y")
                if type == 'xml':
                        return date
                else:
                        return date.__format__("%Y-%m-%d")

        @abstractmethod
        def call(self, method: str, params: dict)-> dict:
                '''
                Metoda na volani API dotazu. Vlozime pozadovanou metodu a parametry a nechame tridu provolat API
                '''
                pass

class JsonApi(Api):
        '''
        Trida pro praci s Sklik API pro specifika volani JSON
        '''
        def call(self, method: str, params: dict)-> dict:
                if isinstance(params, tuple):
                        res = post(self.url + method, json=[*params]).json()
                else:
                        res = post(self.url + method, json=[params]).json()
                return res

class XmlApi(Api):
        '''
        Trida pro praci s Sklik API pro specifika volani XML
        '''
        def call(self, method: str, params)-> dict:
                context = ssl.SSLContext()
                port = client.ServerProxy(self.url, context=context)
                inst = getattr(port, method)
                if isinstance(params, tuple):
                        res = inst(*params)
                else:
                        res = inst(params)
                return res    