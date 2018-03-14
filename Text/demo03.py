#! /usr/bin/env python
# -*- coding: utf-8 -*-
x = raw_input("请输入日期，比如2017-04-04:")
year = int(x[:4])
month = int(x[5:7])
day = int(x[9:10])
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
data = sum(month_day[:(month-1)],day)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if month > 2:
        data = data + 1
print "这是今年的第 %d 天"% (data)
i = data % 7
d = data / 7
if (i == 0):
    print "这是今年的第 %d 周"% (d)
else:
    print "这是今年的第 %d 周" % (d+1)