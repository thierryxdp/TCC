def posLetra(frase,letra,n):
    limitador= 0
    if str.count(frase,letra) < n:
        return -1
    while limitador != n-1:
        frase = str.replace(frase,letra,' ',1)
        limitador += 1
    return str.index(frase,letra)