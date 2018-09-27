def compteur_chiffre(suite_chiffre,indice):
    l=suite_chiffre[indice] ; i=indice-1
    while suite_chiffre[i]==l and i>0 :
        i-=1
    return indice-i

def terme_suivant(suite_chiffre):
    indice=len(suite_chiffre)-1 ; terme=0; compteur=0
    while indice>=0:
        a=suite_chiffre[indice] ;
    
        if a=="1" and indice==1:
                terme+=11*10**compteur
        elif a=="2" and indice==1:
                terme+=12*10**compteur
        elif a=="3" and indice==1:
                terme+=13*10**compteur
        elif a=="1" and indice==2:
                terme+=21*10**compteur
        elif a=="2" and indice==2:
                terme+=22*10**compteur
        elif a=="3" and indice==2:
                terme+=23*10**compteur
        elif a=="1" and indice==3:
                terme+=31*10**compteur
        elif a=="2" and indice==3:
                terme+=32*10**compteur
        compteur+=2 ;    indice-=compteur_chiffre(suite_chiffre,indice); print(indice)
    return terme
ass=112
ass=str(ass)
print(terme_suivant(ass))