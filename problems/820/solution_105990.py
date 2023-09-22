def posLetra(strg,l,n):
    contador1=0
    contador2=0
    tamstr=len(strg)
    
    while contador1<tamstr:
        if strg[contador1]==l:
            contador2=contador2+1
        if contador2==n:
            break
        contador1=contador1 + 1
    if contador2<n:
        return -1
    return contador1