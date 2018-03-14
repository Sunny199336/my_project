#! /usr/bin/env python
# -*- coding: utf-8 -*-
def printme(str):
    "打印任意传入的字符串"
    print str
    return

printme("调用定义函数")
printme("再次调用同一个函数")

str = input("请输入查询日期：（格式如20170404）：")
y = int(str[:4])
m = int(str[4:6])
d = int(str[6:8])
m_d = [31,28,31,30,31,30,31,31,30,31,30,31]
day = sum(m_d[:(m-1),d])
if (y % 4 == 0 and y % 100 !=0) or (y % 400 == 0):
    if m > 2:
        day = day + 1
print "这是今年的第 %d 天"% (day)
