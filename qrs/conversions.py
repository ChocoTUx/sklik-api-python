'''
Request what havent any category or are somehow special
'''
import sys
sys.path.append('..')
from src.setup import Api, Root


class Conversions:
    '''
    All stuff about request category Conversions
    '''
    def conversions_list(self):
        root = Root('json', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user)
            
        response = api.call('conversions.list', params)
        print (response)

        root.logout()

    def conversions_convTypes(self):
        root = Root('json', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user)
            
        response = api.call('listConversionTypes', params)
        print (response)

        root.logout()


    def conversions_create(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
        [{ 'name': 'Konverze',  'value': 1, 'color': 'ffffff',  'conversionTypeId': 123456},
            { 'name': 'Konverze e-shop',  'value': 123456789, 'color': 'ffffff',  'conversionTypeId': 123456},
            { 'name': 'Text',  'value': None, 'color': 'ffffff',  'conversionTypeId': 123456}
        ])
            
        response = api.call('conversions.create', params)
        print (response)

        root.logout()

conversions = Conversions()
conversions.conversions_list()