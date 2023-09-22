def posLetra(frase,l,n):
    i=0
    r=()
    while i < len(frase):
        if l==(frase[i]):
            r=r+i 
        i=i+1
    posicao=r[n-1]
    return posicao