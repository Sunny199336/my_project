#! /usr/bin/env python
# -*- coding: utf-8 -*-
l = [8,5,3,1]   #降序排列
def judge(param):
    c1 = 0
    c2 = 0
    for idx,value in enumerate(l)：

    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            c1+=1
        elif l[i]>l[i+1]:
            c2+=1
        else:
            c1+=1
            c2+=1
    if c1 == len(l)-1:
        print "UP"
    elif c2== len(l)-1:
        print "DOWN"
    else:
        print "WRONG"
    return

print judge(l)
