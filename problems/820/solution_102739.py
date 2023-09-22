def posLetra(palavra,letra,n):
    x=str.find(letra)
    while x> 0 :
        pos= str.find(letra,x+1)
        n-=1
    return x