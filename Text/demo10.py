#! /usr/bin/env python
# -*- coding: utf-8 -*-
def sub_sort(array,low,high):   #定义一个抓取索引然后快排的方法
    key = array[low]
    while low < high:
        if low < high and array[high] >= key:
            high -= 1
        elif low < high and array[high] < key:
            array[low] = array[high]
            low +=1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high): #分别对key两边的序列递归调用快排方法
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


if __name__ == '__main__':
    array = [2,5,7,8,94,4,3,4,656]
    print array
    quick_sort(array,0,len(array)-1)
    print array
