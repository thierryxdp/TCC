def posLetra(frase,letra,num):
    if num < list.count(list(frase),letra):
        return -1
    a= str.replace(frase,num,'', num-1)
    return str.index(a,letra)