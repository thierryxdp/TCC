def faltante(lista):
    i = 0
    retorno = 1
    lista.sort()
    while i<(len(lista)-1):
        if lista[0] == 1 and (lista[i]+1) != lista[i+1]:
            retorno = lista[i]+1
        if lista[0] == 1 and (lista[i]+1) != lista[i+1]:
            retorno = len(lista)+1
        i=i+1
    return retorno