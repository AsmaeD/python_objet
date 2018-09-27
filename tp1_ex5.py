def fibo(n):
    if n==0:
        resultat =[1,1]
        return resultat
    else:
        resultat=fibo(n-1)
    return [resultat[1], resultat[0]+resultat[1]]

def fibo2(n):
    u=[]
    for i in range(0,n+1):
        if i==0 or i==1:
            u+=[1]
        else:
            u+=[u[i-1]+u[i-2]]
    return u

def aff(n):
    p=fibo(n)
    print(f"La valeur de la suite au terme {n} vaut {p[0]}")

