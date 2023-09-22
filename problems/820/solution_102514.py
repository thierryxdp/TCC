def posLetra(frase,letra,n):
    if frase.count(letra)<n:
        return -1
    else:
        frase.find(letra,n)