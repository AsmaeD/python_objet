import numpy as np

def divi(n,i):
    return (n%i)==0

def extract_div(n):
    L=[]
    for i in range (1, int(1+n/2)):
        if divi(n,i):
            L+=[i]
    return L
        
def parfait(n):
    L=[]
    for i in range (1,n):
        if np.sum(extract_div(i))==i:
            L+=[i]
    return L

#il  a d'autres moyens de divisions entiere (//) on peut diviser le temps de cacul en deux mais c'est deja fait
    #j'avais utilisé int (1+n/2)mais en rajoutant les diviseurs par deux on optimise cependant il ne marche plus
    


def con_amicaux(n,m):
    if (np.sum(extract_div(n))==m) and (np.sum(extract_div(m))==n) :
        return 1
    else:
        return 0

def amicaux(n):
    l=[];s=0
    for i in range(1, n):
        s=np.sum(extract_div(i))
        if (np.sum(extract_div(s))==i) and (i<s<n):
                l+=[[i, s]]
    return l
    
#ceci est la version corrigée du prof car plus optimisée de loin en enlevant une boucle