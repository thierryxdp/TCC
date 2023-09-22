def posLetra(frase,letra,n):
    i = 0
    acumulador= 0
    while i<len(frase) and acumulador<n:
        if frase[i] == letra:
            acumulador=acumulador +1
        i = i + 1
    if acumulador<n:
        return str(acumulador)+str(letra)
    else:
        return -1