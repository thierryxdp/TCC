def faltante(lista):
    i = 0
    retorno = 0
    lista.sort()
    while i<(len(lista)-1):
        if (lista[i]+1) != lista[i+1]:
            retorno = lista[i]+1
        i=i+1
    return retorno