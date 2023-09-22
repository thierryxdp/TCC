def posLetra(frase,letra,n):
    if frase.count(letra)<n:
        return -1
    i=0
    p=0
    x=0
    while i<n:
        if letra==frase[p]:
                x=len(frase[0:p])
                i=i+1
        p=p+1
    return x+1