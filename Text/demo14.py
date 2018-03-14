#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" rule1：你从输入中读入的一个单词，如果这个单词和当前行已有的长度加起来不超过80，则将该单词输出到当前行，否则另起一行，将该单词输出到下一行的开头；
    rule2：如果你从输入中读到的是,则换行
    rule3：如果你从输入中读到的是空行,则另起一行输出80个'-'（如果当前正好在新行的开始，则直接输出80个'-'），并再次换行到新行的开始。
    rule4：单词之间以一个空格分开。"""

def parse(html):

    # 将逗号使用标签替换
    html = html.replace(',',' <br> ')
    # 使用换行进行分割
    lines = html.split('\n')
    words = []
    for line in lines:
        temp = line.split(' ')
        for word in temp:
            # 如果分隔开的字符串中不含空格则添加到words列表中
            if word != ' ' and word != '':
                words.append(word)
    return words

def print_words(words):
    line = ''
    for word in words:
        # 出现换行符则换行输出
        if word == '<br>':
            print line
            line = ''
        #出现水平线标签且该行有单词则输出然后打印水平线
        elif word == '<hr>':
            if len(line) != 0:
                print line
                line = ''
            print '-' * 80
        #每行长度大于80则换行输出，否则空格补全
        elif len(line) + len(word) > 80:
            print line[:-1]
            line = word + ' '
        else:
            line = line + word + ' '
    if len(line) != 0:
        print line[:-1]

html='Hallo, dies ist eine ziemlich lange Zeile, die in Html aber nicht umgebrochen wird. <br> ' \
     'Zwei <br> <br> produzieren zwei Newlines. Es gibt auch noch das tag <hr> was einen Trenner darstellt.Zwei ' \
     '<hr> <hr> produzieren zwei Horizontal Rulers.Achtung       ' \
     'mehrere Leerzeichen irritieren Html genauso wenig wie mehrere Leerzeilen.'

words = parse(html)
print words
print_words(words)