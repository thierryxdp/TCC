def posLetra(frase,letra,n):
    i = str.count(frase)
    if i>n:
        return str.index(frase,letra,n)
    else:
        return -1