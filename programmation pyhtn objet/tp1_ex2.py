#nombre chanceux
import numpy as np 

def conf_div(n,i):
    if n%i==0:
        return 1
    else:
        return 0

def premier(n):
    for i in range(2,int(np.sqrt(n))):
        if conf_div(n,i):
            return 0
    return 1

def appartient_pas(i,L):
    for j in range (0,len(L)):
        if L[j]==i:
            return 0
    return 1

def chanceux(n):
    for i in range(0,n-1):
        if not premier(n+i*i+i):
            return 1
    return 0

def nb_chan(n):
    l=[];j=0;p=2
    for i in range(1,n):
       if chanceux(i):
           l+=[i]
    return l
        
