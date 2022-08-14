#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:42:38 2021

@author: lab05
"""
import pandas as pd
import pymysql
#%%
connection = pymysql.connect(host='localhost',user='lab04',password='MIS5502',db='webscraper',
                             charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql= " SELECT * FROM forbes"
        df = pd.read_sql(sql, connection)
        
finally:
    connection.close()
#%%
df.to_csv('/home/lab04/webscraper/forbes.csv')
#%%
print(len(df))