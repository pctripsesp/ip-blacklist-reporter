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


#LAST IP GETTER
def last_ip_getter():
    try:
        f = open("last_ip_reported.data", 'r')
        last_ip = f.readline()
        print (last_ip + " IS THE LAST IP REPORTED")
        return (last_ip)
        f.close()

    except:
        print ("NO LAST IP REPORTED FILE FOUND")


#LAST IP SETTER
def last_ip_setter(last_ip):
    f = open("last_ip_reported.data", 'w')
    f.write(last_ip)
    f.close



#THIS USES IP LIST FROM "blackListMaker.py" to send report
def reportFromBL():
    last_ip_reported = last_ip_getter()
    IP_BList = blackListMaker.makeBL()
    IP_BList_len = len(IP_BList)
    c=0

    while True:
        
        #CHECKS 60 REQUESTS/MIN LIMIT
        if c%61==0 and c!=0:         
            print(str(c)+'/'+str(IP_BList_len)+' REPORTED')
            print('sleeping 1 minute')
            sleep(62)
        
        # CHECKS IP_LIST LIMIT LENGTH
        if c+1 == IP_BList_len:
            print("ALL IP'S HAS BEEN SUCCESFULLY REPORTED")
            break

        # CHECKS LAST IP REPORTED TO STOP REPORTING
        if last_ip_reported  == IP_BList[c]:
            print(last_ip_reported +" HAS BEEN ALREADY REPORTED")
            break

        data = report_IP(IP_BList[c])
        c+=1

        # REPORTED OK
        try:
            if data['success'] == True:
                print(data['ip']+" REPORTED")
		last_ip_setter(data['ip'])
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
