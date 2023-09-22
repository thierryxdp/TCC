def repetidos(lista):
    i = 0
    retorno = 0
    while i < len(lista):
        retorno += list.count(lista,lista[i])
        i += 1
    return retorno