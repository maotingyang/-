# -*- coding: utf-8 -*-
"""
L為一個充滿整數的List；f為一個未知函數，輸入為整數，輸出為整數，
g為一個未知函數，輸入為整數，輸出為布林值
目的：檢查每一個L裡的整數index，若g(f(index))為真，留下此整數，
其他整數皆從L刪除，最後回傳L裡的最大值。
"""

def applyF_filterG(L, f, g):
    copyL = L.copy()
    for index in copyL:
        if g(f(index)) is False:
            L.remove(index)
        for index in L:
            while L.count(index) > 1:
                L.remove(index)
    if len(L) == 0:
        return -1
    else:
        return sorted(L)[len(L)-1]
    
def f(i):
    return i
def g(i):
    return i < 5

L = [1,0,-1,2,3,5,6,7,2,3,4]
print(applyF_filterG(L, f, g))
print(L)     