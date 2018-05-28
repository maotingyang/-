# -*- coding: utf-8 -*-

"""
Created on Tue May  1 05:39:05 2018

找尋符合字母順序最長的字串，若有長度相同者，選最早出現者

"""

s = "zzefghijklabcdef" 
#假設一個S字串

slength = len (s)
icount = 1
rcount = 1
ranswer = ""
ianswer = ""
x=0

if slength == 1:
    ianswer = s
else:
    for i in s:
        if  icount < slength and i <= s[icount]:
            icount += 1
        
        else:
            ianswer = s[0:icount]
    
    for r in s:
        if  rcount < slength and r <= s[rcount]:
            rcount += 1
                    
        else:        
            ranswer = s[x:rcount]
            if len(ranswer) > len(ianswer):
                ianswer = ranswer
            x = rcount
            rcount += 1
        
    
print ("Longest substring in alphabetical order is: "+ianswer)