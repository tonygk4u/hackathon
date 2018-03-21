# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 12:25:57 2018

@author: Tony.George
"""

import os 
import pandas as pd
import pandas_profiling


path = 'C:/Users/tony.george/Documents/docs/hackathon/'#input("Please enter path:")
os.chdir(path)


df1 = pd.read_csv('CRS_Test_Data29112017 223508.csv',encoding = "ISO-8859-1")

df1.groupby(['Account Holder Street Name', 'Account Holder District Name'])['Account Party ID'].nunique()