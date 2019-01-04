'''
Request what havent any category or are somehow special
'''
import sys
sys.path.append('..')
from src.setup import Api, Root


import pytest
import base64

class Ads:
    '''
    All stuff about request category Client
    '''
    def ads_create_combi(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()
        tpe = 'xml'

        land = open('./../img/600_314.jpg',"rb").read()
        if tpe is 'json':
            land = base64.b64encode(land).decode()
        square = open('./../img/square.jpg',"rb").read()
        if tpe is 'json':
            square = base64.b64encode(square).decode()
        landLogo = open('./../img/1200_300.jpg',"rb").read()
        if tpe is 'json':
            landLogo = base64.b64encode(landLogo).decode()

        params = (user,
            [{
                'groupId': 123456,
                'adType': 'combined',
                'image': land,
                'imageLandscapeLogo': landLogo,
                'imageLogo': square,
                'imageSquare': square,
                'shortLine': 'Digitální fotoaparáty',
                'longLine': 'Prodejce nejkvalitnějších fotoaparátů',
                'finalUrl': 'https://www.megapixel.cz/digitalni-fotoaparaty',
                'companyName': 'Digitalni Foto s.r.o.',
                'description': 'Nejnižší ceny, Značky Nicon, Canon, Rollei',
                'status': 'active'
            }])
            
        response = api.call('ads.create', params)
        print (response)

        root.logout()
    
    def ads_create_eeta(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        tpe = 'xmll'
        #86226041
        params = (user,
            [{
                'groupId': 123456,
                'adType': 'eta',
                'description': 'Tadypopisek 1, který má podstatně delší test ěščřžýáíéúů a tudíž délka devadesát znaků'+tpe,
                'description2': 'Tady je popisek 2, který má podstatně delší test ěščřžýáíéúů a tudíž délka devadesát znaků',
                'finalUrl': 'http://www.chocotux.cz',
                'mobileFinalUrl': 'http://www.chocotux.cz/m',
                'headline1': 'Tohle Titulke1delka tricet'+tpe,
                'headline2': 'Toe Titulke 2 a delka tricet',
                'headline3': 'Tohle Titulke 3 a delka tricet',
                'path1': 'cestajedna',
                'path2': 'cestadva'
            }])
            
        response = api.call('ads.create', params)
        print (response)

        root.logout()

    def ads_update_eeta(self):
        root = Root('xml', 'default')

        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            [{
                'id': 123456,
                'adType': 'eta',
                'status': 'suspend',
                'headline3': 'Vyber si sám',
                'description2': 'Už nepomáháme s výběrem.'
            }])
        
        response = api.call('ads.update', params)
        print (response)

        root.logout()

    def ads_list_eeta(self):
        root = Root('xml', 'default')

        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {'group':{'ids': [123456]}},{'limit': 10, 'offset': 0})
        
        response = api.call('ads.list', params)
        print (response)

        root.logout()

    def ads_report_eeta(self):
        root = Root('xml', 'default')

        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            [{
                'id': 123456,
                'adType': 'eta',
                'status': 'suspend',
                'headline3': 'Vyber si sám',
                'description2': 'Už nepomáháme s výběrem.'
            }])
        
        response = api.call('ads.update', params)
        print (response)

        root.logout()   
ads = Ads()
ads.ads_list_eeta()