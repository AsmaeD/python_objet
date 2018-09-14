import tp1_revision

import numpy as np

#Exercice 1 : 

def est_divisible(n,i):
    return (n%i)==0

def extract_div(n):
    l=[]
    for i in range (1,1+int(n/2)):
            if est_divisible(n,i):
                l+=[i]
    return l

def nb_parfait(n):
    liste_nb=[]
    for i in range(1,n):
        if np.sum(extract_div(i))==i:
            liste_nb+=[i]
    return liste_nb

def sont_amicaux(n,m):
    return (np.sum(n)==m) and (np.sum(m)==n)
        
def nb_amicaux(n):
    liste_nb=[]
    for i in range(1,n):
        s=np.sum(extract_div(i))
        if (i==np.sum(extract_div(s))) and (i<s<n):
            liste_nb+=[[i,s]]
    return liste_nb

#x=input("Tapez un nombre et nous vous dirons quels seront les nombres parfaits \n")
#x=int(x)
#print("Les nombres parfaits sont ", nb_parfait(x), "et les nombres amicaux sont ", nb_amicaux(x))


#Exercie 2 :


def est_premier(n):
    for i in range(2, 1+int(np.sqrt(n))):
        if n%i==0:
            return 0
    return 1

def est_chanceux(p):
    for i in range(0,p-1):
        if not est_premier (p+i*i+i):
            return 0
    return 1

def nb_chanceux(n):
    nb_liste=[]
    for i in range (1,n):
        if est_chanceux(i):
            nb_liste+=[i]
    return nb_liste

#Exercice 3:
    
def extract_cube(n):
    k=1 ; liste_cube=[]
    while (k**3)<=n:
        liste_cube+=[k]
    return liste_cube

def est_egale(n,a,b):
    return n==(a**3)+b**3

x=tp1_revision.est_premier(10)



