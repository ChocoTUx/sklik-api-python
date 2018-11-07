'''
Request what havent any category or are somehow special
'''
from setup import Api, Root

class Client:
    '''
    All stuff about request category Client
    '''
    def client_stats(self):
        root = Root('xml', 'default')
        #struct user (struct base for other requests)
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                'dateFrom' : api.date_trans("1.11.2017", 'xml'),
                'dateTo' : api.date_trans("4.11.2018", 'xml'),
                'granularity': 'total'
            })            
        response = api.call('client.stats', params)
        print (response)

        root.logout()

client = Client()
client.client_stats()