def posLetra(frase,letra,n):
    i = 0 
    r = 0
    while  i <= n :
        if letra in frase:
            r = str.index(frase,letra,r)
        i=i+1
    return r


r1 = str.index(frase,letra)
r2 = str.index(frase,letra,r1+1)
r3 = str.index(frase,letra r2+1)