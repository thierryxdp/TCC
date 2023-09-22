def posLetra(frase,letra,n):
    i = 0 
    r = 0
    while  i <= n :
        if letra in frase:
            r = str.index(frase,letra,r+1)
        i=i+1
    return r