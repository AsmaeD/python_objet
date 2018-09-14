import numpy as np

def conf(k,l,n):
    return k+l==n

def cube_liste(n):
    m=[];s=0
    b=1+int(n**(1/3))
    for i in range (1,b):
        icube=i**3
        for j in range(i+1,b):
            s=icube + j**3
            if s<=n: 
                for k in range(i+1, b):
                    kcube=k**3
                    for l in range(k+1,b):
                        if (l**3 + kcube == s):
                            m+=[s,[i,j],[k,l]]
    return m

