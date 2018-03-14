#! /usr/bin/env python
# -*- coding: utf-8 -*-
l = [2,5,80,3]  #升序排列
# print(sorted(l))

for i in range(len(l)): #冒泡排序
    for j in range(len(l)-1):
        if l[j] >l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print l