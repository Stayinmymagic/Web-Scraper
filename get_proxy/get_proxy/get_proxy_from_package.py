#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:04:28 2021

@author: notfunny6889
"""

from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

scrapper = Scrapper(category='', print_err_trace=False)
# Get ALL Proxies According to your Choice
data = scrapper.getProxies()
#%%
proxylist = []
# Print These Scrapped Proxies
print("Scrapped Proxies:")
for item in data.proxies:
    item
    #proxylist.append({'ip':item.ip, 'port':item.port})
    #print('{}:{}'.format(item.ip, item.port))

# Print the size of proxies scrapped
print("Total Proxies")
print(data.len)

# Print the Category of proxy from which you scrapped
print("Category of the Proxy")
print(data.category)
#%%
import requests
r = requests.get('https://httpbin.org/ip', )
proxies=proxy
#%%
import json
with open('/Users/notfunny6889/get_proxy/proxy.json', 'w') as fout:
    json.dump(proxylist , fout)