#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
s='2014-01-01'
format = '%b %d %Y'
dt=datetime.datetime.strptime(s,format)
print dt.date()