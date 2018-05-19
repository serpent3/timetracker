#!/usr/bin/env python3
# -*- coding: utf-8 -*-
counter = 0
with open('q', 'r') as q:
    l = q.readlines()
    for i in range(len(l)):
        if float(l[0].split('\n')[0]) - float(l[0].split('\n')[0]) < 3:
            counter += 2
            print (counter)
        #print(l[i])
        
        
        
    #print(q)
#    
#    for line in q:
#        #print (line)
#        l = int(line)
# if int(l[i].split('/')) - int(l[i+1].split('/')) == 1:
        
        
        