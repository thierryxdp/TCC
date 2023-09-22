def posLetra(frase,letra,n):
    y=0
    x=-1
    while y<n:
        if letra==frase[x]:
            y=y+1
        x=x+1
    return x