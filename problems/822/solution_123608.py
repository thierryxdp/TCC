def repetidos(lista):
    i = 1
    lista_nova = list()
    while (i<len(lista)):
        if (lista[i] == lista[i-1]):
            lista_nova += (lista[i],)
    i += 1
    else
        lista_nova = lista[i]
    
    return lista_nova