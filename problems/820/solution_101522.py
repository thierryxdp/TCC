def posLetra(string,letra,n):
    k=string.find(letra)
    while k>=0 and n>1:
        k=string.find(letra,k+1)
        n=n-1
    return k