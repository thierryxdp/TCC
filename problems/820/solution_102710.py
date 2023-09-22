def posLetra(frase,letra,num):
    if num > str.count(frase,letra):
        return -1
    else:
        a= str.replace(frase,letra,' ', (num -1))
    return str.index(a,letra)