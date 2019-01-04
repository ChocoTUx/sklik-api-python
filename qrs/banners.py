'''
Request what havent any category or are somehow special
'''
import sys
sys.path.append('..')
from src.setup import Api, Root


class Banners:
    '''
    All stuff about request category Client
    '''
    def banners_update(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        banner = open('./img/300_300.jpg',"rb").read()
        params = (user,
            [{
                'id': 123456,
                'name': 'Tady je zmena',
                'file': banner,
            }])            
        response = api.call('banners.update', params)
        print (response)

        root.logout()

banners = Banners()
banners.banners_update()