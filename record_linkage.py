# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:16:31 2018

@author: Tony
"""
#Refer http://recordlinkage.readthedocs.io/en/latest/notebooks/data_deduplication.html
import pandas as pd
import recordlinkage

raw_ds = pd.read_csv('F:\Data_Scientist\hackathon-master\CRS_Test_Data29112017 223508.csv',encoding='ISO-8859-1')
raw_ds_sliced = raw_ds[['Account Party ID','Account Holder First Name','Account Holder Last Name','Account Holder City','Account Holder Date of Birth']]
#print(raw_ds.head())
indexer = recordlinkage.BlockIndex(on='Account Party ID')
pairs = indexer.index(raw_ds_sliced)

#print (len(pairs))
compare_cl = recordlinkage.Compare()

compare_cl.exact('Account Party ID', 'Account Party ID', label='Account Party ID')
#compare_cl.string('Account Holder First Name', 'Account Holder First Name', method='jarowinkler', threshold=0.85, label='Account Holder First Name')
#compare_cl.string('Account Holder Last Name', 'Account Holder Last Name', method='jarowinkler', threshold=0.85, label='Account Holder Last Name')
compare_cl.exact('Account Holder Date of Birth', 'Account Holder Date of Birth', label='Account Holder Date of Birth')
#compare_cl.exact('Account Holder City', 'Account Holder City', label='Account Holder City')


features = compare_cl.compute(pairs, raw_ds_sliced)
features.head(20)
features.describe()

# Sum the comparison results.
features.sum(axis=1).value_counts().sort_index(ascending=False)

matches = features[features.sum(axis=1) > 1]

print(len(matches))
print(matches.head(20))