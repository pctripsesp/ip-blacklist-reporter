#!/usr/bin/env python
# -*- coding: utf-8 -*-
# THIS SCRIPT PRINTS IP ADDRESSES FROM SERVER'S LOG FILE LIKE: 
'''
Warning,Sistema,2017/11/01 17:22:33,SYSTEM,Host [218.67.107.3] was blocked via [SSH].

Warning,Sistema,2017/11/01 17:19:31,SYSTEM,Host [59.27.35.119] was blocked via [SSH].

Warning,Sistema,2017/11/01 17:11:42,SYSTEM,Host [92.111.181.206] was blocked via [SSH].
'''


#LOG FILE PATH
filename = "syslog_2017-11-1-17_30_31.csv"

with open(filename) as f:
    while True:
        line = f.readline()
        if "was blocked via" in line:
            start = line.find('[') + 1
            end = line.find(']', start)
            print(line[start:end])	

        if not line:
            break	
