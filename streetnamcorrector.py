# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:30:26 2018

@author: Tony
"""

import os 
import pandas as pd
import difflib

path = 'E:/My Lab/hackathon/'#input("Please enter path:")
os.chdir(path)


df1 = pd.read_csv('CRS_Test_Data29112017 223508.csv',encoding = "ISO-8859-1")

#word = 'KPr CrescenX'

master = df1.groupby(['Account Holder Street Name', 'Account Holder District Name']).size().reset_index(name='count')
#master_district = master.loc[master['Account Holder District Name'] == 'YORK']
#master_district = master_district.loc[master_district['count'] >= 5]['Account Holder Street Name']
#difflib.get_close_matches(word, master_district, n=1)

df1['Corrected_Street']='NA'

for index, row in df1.iterrows():
    district = row['Account Holder District Name']
    master_district = master.loc[master['Account Holder District Name'] == district]
    master_street = master_district.loc[master_district['count'] >= 5]['Account Holder Street Name']
    
    if (row['Account Holder Street Name'] in list(master_street)):
        df1.set_value(index,'Corrected_Street',row['Account Holder Street Name'])
    else:
        Corrected_street = difflib.get_close_matches(row['Account Holder Street Name'], master_street, n=1)
        df1.set_value(index,'Corrected_Street',Corrected_street)
        print(index,Corrected_street)
 
df1.to_csv('corrected_streetname.csv')         
    