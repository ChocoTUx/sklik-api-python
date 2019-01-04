'''
Class whit API Call examples
'''
import sys
sys.path.append('..')
from src.setup import Api, Root
from datetime import datetime
import time

class Campaigns:
    def campaigns_report_nullfinder(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                "dateFrom" : api.date_trans("01.02.2018", "xml"),
                "dateTo" : api.date_trans("19.11.2018", "xml")
            })            
        response = api.call('campaigns.createReport', params)
        print (response)

        count = response['totalCount']
        offset = 0
        while count > 0:
            params = (user, response['reportId'],
                {
                    'offset': offset,
                    'limit': 10,
                    'allowEmptyStatistics': True,
                    'displayColumns': ["id", "status", "impressions", "deleted", "name"]
                })
            response = api.call('campaigns.readReport', params)
            if not response['status'] == 500:    
                print (offset)
                for report in response['report']: 
                    for name, value in report.items():
                        if value == "nil" or value == "null" or value is None:
                            print("chyba||"+str(report))
                            print(response['reportId'])
            offset += 10
            count -= 10
        root.logout()


    def campaigns_update(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            [{
            'id': 123456,  
            'name': 'SEA>K-M>Categories>Broad',
            'excludedSearchServices': [],     
            'adSelection': 'weighted',
            'type': 'fulltext',
            'premise': {'id': 123456}
            }])            
        response = api.call('campaigns.update', params)
        print (response)

        root.logout()



campaigns = Campaigns()
campaigns.campaigns_update()

# For cycle testing
# for x in range(30):
#     print("Jedu kolo cislo: "+ str(x))
#     campaigns.campaigns_report_nullfinder()
#     time.sleep(6)