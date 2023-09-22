def posLetra(frase,letra,n):
    limitador= 1
    if str.count(frase,letra) < n:
        return -1
    while limitador != n:
        frase = str.replace(frase,letra,' ',1)
        limitador += 1
    return str.index(frase,letra)