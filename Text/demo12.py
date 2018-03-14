#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib  #调用uerllib
import webbrowser
url = 'http://www.qq.com/'
content = urllib.urlopen(url).read()
open('test.html','w').write(content)  #写入到test.html文件中
webbrowser.open_new_tab('test.html') #打开写入的文件