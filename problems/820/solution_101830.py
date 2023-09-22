def posLetra(frase,letra,n):
    x=1
    i=0
    while x<=n:
        a=str.find(frase,letra,i,)
        i=str.find(frase,letra,i,)+1
        x=x+1
    return a