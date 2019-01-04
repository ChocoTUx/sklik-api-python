'''
Class whit API Call examples
'''
import sys
sys.path.append('..')
from src.setup import Api, Root

from datetime import datetime
import time

class Groups:
    def groups_report(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                'campaign' : {'ids': [123456]},                
                "dateFrom" : datetime.strptime("14.11.2018", "%d.%m.%Y"),
                "dateTo" : datetime.strptime("14.11.2018", "%d.%m.%Y")
            })            
        response = api.call('groups.createReport', params)
        print (response)

        params = (user, response['reportId'],
            {
                'offset': 0,
                'limit': 5000,
                'allowEmptyStatistics': True,
                'displayColumns': ['impressions','clicks','conversions','conversionValue','avgPos','avgCpc','clickMoney','id','campaign.id']
            })
        response = api.call('groups.readReport', params)
        print (response)    

        root.logout()
    
    def groups_report2(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()
        print(user)
        params = (user,
            {
                'campaign' : {'ids': [123456]},
                #'ids': [123456],
                "dateFrom" : datetime.strptime("01.01.2014", "%d.%m.%Y"),
                "dateTo" : datetime.strptime("19.11.2018", "%d.%m.%Y")
            })            
        response = api.call('groups.createReport', params)
        print (response)

        params = (user, response['reportId'],
            {
                'offset': 0,
                'limit': 5000,
                'allowEmptyStatistics': True,
                'displayColumns': ["id", "status", "maxCpc", "deleted", "name", "campaign.name", "campaign.id"]
            })
        response = api.call('groups.readReport', params)
        print (response)    

        root.logout()

    def groups_create(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()
        print(user)
        params = (user,
            [{'status': 'active', 'cpcContext': 500, 'cpc': 500, 'name': 'Test divocha', 'campaignId': 123456}, {'status': 'active', 'cpcContext': 500, 'cpc': 500, 'name': 'Test nedivocha', 'campaignId': 123456}]
        )            
        response = api.call('groups.create', params)
        print (response)  

        root.logout()

    def groups_report_nullfinder(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                "dateFrom" : api.date_trans("01.02.2018", "xml"),
                "dateTo" : api.date_trans("19.11.2018", "xml")
            })            
        response = api.call('groups.createReport', params)
        print (response)

        count = response['totalCount']
        offset = 0
        while count > 0:
            params = (user, response['reportId'],
                {
                    'offset': offset,
                    'limit': 5000,
                    'allowEmptyStatistics': True,
                    'displayColumns': ["id", "status", "maxCpc", "deleted", "name", "campaign.name", "campaign.id"]
                })
            response = api.call('groups.readReport', params)
            if not response['status'] == 'error': 
                #print (response)    
                print (offset)
                breakk = False
                for report in response['report']: 
                    for name, value in report.items():
                        if value == "nil" or value == "null" or value is None:
                            print("chyba||"+str(report))
                            print(datetime.now())
                            print(response['reportId'])
                            breakk = True
                            break
                    for name, value in report['campaign'].items():
                        if value == "nil" or value == "null" or value is None:
                            print("chyba||"+str(report))
                            print(datetime.now())
                            print(response['reportId'])
                            breakk = True
                            break
                    if breakk is True:
                        breakk = False
                        break
            #sys.exit('konec')
            offset += 5000
            count -= 5000
        root.logout()

    def groups_report_nullfinder_c(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()

        params = (user,
            {
                "dateFrom" : api.date_trans("01.02.2018", "xml"),
                "dateTo" : api.date_trans("19.11.2018", "xml")
            })            
        response = api.call('groups.createReport', params)
        print (response)
        iterator = 0
        totalCount = response['totalCount']
        while iterator < 50:
            count = totalCount            
            offset = 0
            while count > 0:
                params = (user, response['reportId'],
                    {
                        'offset': offset,
                        'limit': 5000,
                        'allowEmptyStatistics': True,
                        'displayColumns': ["id", "status", "maxCpc", "deleted", "name", "campaign.name", "campaign.id"]
                    })
                response = api.call('groups.readReport', params)
                if not response['status'] == 'error': 
                    #print (response)    
                    print (iterator)
                    for report in response['report']: 
                        for name, value in report.items():
                            if value == "nil" or value == "null" or value is None:
                                print("chyba||"+str(report))
                                print(response['reportId'])
                        for name, value in report['campaign'].items():
                            if value == "nil" or value == "null" or value is None:
                                print("chyba||"+str(report))
                                print(response['reportId'])
                #sys.exit('konec')
                offset += 5000
                count -= 5000
            iterator += 1
        root.logout()

    def groups_list(self):
        root = Root('xml', 'default')
        
        user = root.get_logged_user_struct('default')
        api = root.get_api()
        
        params = (user,
            {},
            {
                'offset': 0,
                'limit': 300,
                'displayColumns': ['name','sensitivity','status','statusId','campaign.actualClicks','campaign.automaticLocation','campaign.adSelectionId','campaign.createDate','campaign.context','campaign.deleteDate','campaign.deleted','campaign.deviceDesktop','campaign.deviceTablet','campaign.deviceMobil','campaign.deviceOther','campaign.endDate','campaign.fulltext','campaign.id','campaign.name','campaign.paymentMethodId','campaign.startDate','campaign.status','campaign.statusId','campaign.totalClicks','campaign.totalBudgetFrom','campaign.totalClicksFrom']

            }
        )       
        response = api.call('groups.list', params)
        print (response)

        root.logout()

groups = Groups()
# for x in range(30):
#     print("Jedu kolo cislo: "+ str(x))
#     groups.groups_report_nullfinder()
#     time.sleep(6)
groups.groups_list()
#groups.groups_create()