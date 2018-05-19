#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from conf import interval, log

counter = 0
with open(log, 'r') as log:
    l = log.readlines()
    for i in range(len(l)):
        if float(l[i].split('\n')[0]) - float(l[i].split('\n')[0]) < interval + 1:
            counter += interval
    print(counter)
  