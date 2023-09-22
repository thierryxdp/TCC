def posLetra(frase,letra,n):
    if str.count(frase,letra)<n:
        return -1
    elif str.count(frase,letra)>=n:
        return str.index(frase,letra,n)