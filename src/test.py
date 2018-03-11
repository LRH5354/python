# -*- coding: utf-8 -*-
def fact(n):
    if(n==1):
        return n
    return n*fact(n-1)

abc={'a':1,'b':2,'c':3};
for key in abc.itervalues():
    print key

