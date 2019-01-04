'''
Class whit API Call examples
'''
import sys
sys.path.append('..')
from src.setup import Api, Root

from datetime import datetime
import xmlrpc


class Keywords:
    def keywords_createReport(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                "dateFrom" : datetime.strptime("06.12.2018", "%d.%m.%Y"),
                "dateTo" : datetime.strptime("06.12.2018", "%d.%m.%Y")
            }, {
                "statGranularity": 'daily'
            })            
        response = api.call('keywords.createReport', params)
        print (response)

        params = (user, response['reportId'],
            {
                'offset': 0,
                'limit': 5000,
                'allowEmptyStatistics': True,
                'displayColumns': ['id']
            })
        response = api.call('keywords.readReport', params)
        print (response)    

        root.logout()

    def keywords_update(self):
        root = Root('json', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()
        params = (user,
            [{
                'id': 123456,
                'cpc': 7000,
            }])
        response = api.call('keywords.update', params)
        print (response)    

        root.logout()
        

keywords = Keywords()
keywords.keywords_createReport()