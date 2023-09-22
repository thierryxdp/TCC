def posLetra(frase,letra,n):
    if str.count(frase,letra)>=n:
        h = str.index(frase,letra,n)
        return str.index(frase,letra,h+1)
    else:
        return -1