#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#USING www.abuseipdb.com API --> YOU NEED TO USE YOURS

'''
REPORT IP https://www.abuseipdb.com/report/json?key=[API_KEY]&category=[CATEGORIES]&comment=[COMMENT]&ip=[IP]
'''

import requests
import blackListMaker
from time import sleep

myAPIKey = '<YOUR_API_KEY>'   #Your API KEY from www.abuseipdb.com

#REPORT IP
def report_IP(ip):
    
    response = requests.get('https://www.abuseipdb.com/report/json?key='+myAPIKey+'&category=18,22&comment=ssh brute force&ip='+ip)
    return response.json()  
            

#THIS USES IP LIST FROM "blackListMaker.py" to send report
def reportFromBL():

    IP_BList = blackListMaker.makeBL()
    IP_BList_len = len(IP_BList)
    c=0

    while True:
        data = report_IP(IP_BList[c])
        c+=1

        #CHECKS 60 REQUESTS/MIN LIMIT
        if c%61 == 0:
            print('sleeping 1 minute')
            sleep(62)
        
        # CHECKS IP_LIST LIMIT LENGTH
        if c == IP_BList_len:
            break

        # REPORTED OK
        try:
            if data['success'] == True:
                print(data['ip']+" REPORTED")
                continue
        except:
            pass

	# LIMIT REPORTS REACHED
        try:
            if '15 minutes' in data[0]['meta']:
                print (data[0]['meta'])
                continue
        except:
            print("DAYLY LIMIT REACHED")
            break

    print("------------------------------")
    print("TOTAL: "+str(c)+" IPs REPORTED")



reportFromBL()
