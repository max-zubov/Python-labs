#!/usr/bin/python

# function for create a dict from two lists
def dictcreate(keylist, vallist):
    keylist=list(set(keylist))
    j=len(vallist)
    return({keylist[i]: vallist[i] if i<j else None for i in range(len(keylist))})

#kl=[ 1,2,3,4,5]
kl=[ 1,2,3,4,5,6,7,8]
vl=['a','b','c','d','e','f']

print(dictcreate(kl,vl))    
