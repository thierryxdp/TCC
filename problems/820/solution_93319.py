def posLetra(frase,letra,n):
    cont=0
    oco=0
    while cont<len(frase):
        if frase[cont]==letra:
            oco+=1
            if oco==n:
                return cont
        cont+=1
    return -1