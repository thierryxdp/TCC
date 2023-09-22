def posLetra(a,b,c):
    indice=0
    x=str.find(a,b,indice)
    while indice<=c:
        z= str.find(a,b,indice)
        indice+=2
    if x>=c:
        return x*c
    else:
        return -1