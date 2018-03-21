# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:50:51 2018

@author: Tony.George
"""

import re
from collections import Counter
import pandas as pd

df1 = pd.read_csv('CRS_Test_Data29112017 223508.csv',encoding = "ISO-8859-1")

def words(text): return re.findall(r'\w+', text.upper())

#WORDS = Counter(words(open('districts.txt').read()))
WORDS = Counter(df1['Account Holder District Name'])

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction_2edit(word): 
    "Most probable spelling correction for word."
    return max(candidates_2edit(word), key=P)

def correction_3edit(word): 
    "Most probable spelling correction for word."
    return max(candidates_3edit(word), key=P)

def candidates_2edit(word): 
    "Generate possible spelling corrections for word."
    #return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    #return set([known(edits2(word)), known(edits3(word))])
    #return (known(edits1(word)) and known(edits2(word)) and known(edits3(word)))
    return (known(edits2(word)))

def candidates_3edit(word): 
    "Generate possible spelling corrections for word."
    #return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    #return set([known(edits2(word)), known(edits3(word))])
    #return (known(edits1(word)) and known(edits2(word)) and known(edits3(word)))
    return (known(edits3(word)))

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return frozenset(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def edits3(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits2(word) for e2 in edits1(e1))


#known_districts = words(open('districts_list.txt').read())
known_districts =  pd.read_csv('districts_list.txt')
i=0
df1['Corrected_District']='NA'
for index, row in df1.iterrows():
   if(row['Account Holder Country']== 'GB'):
       if (row['Account Holder District Name'] not in list(known_districts['NAMES'])):
          Corrected_name = correction_2edit(row['Account Holder District Name']) 
          print(Corrected_name)
          df1.set_value(index,'Corrected_District',Corrected_name)
          
          if (Corrected_name not in list(known_districts['NAMES'])):
              new_corrected_name = correction_3edit(row['Account Holder District Name'])
              df1.set_value(index,'Corrected_District',new_corrected_name)
              #print(i,row['Account Holder District Name'],correction(row['Corrected_District']))
              print(index)
   
df1.to_csv('out2.csv')  
   
