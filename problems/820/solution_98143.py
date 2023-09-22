def posLetra(frase,letra,num):
    lista = list(frase)
    pos = lista.count(letra)
    if pos >= n:
        sub = str.replace(frase,letra,'*', num-1)
        return str.find(sub,letra,0,-1)
    else:
        return -1