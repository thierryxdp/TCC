def insere(lista_numero,n):
    indice = list.index(lista_numero,n)
    ordenada_nova = list.insert(lista_numero,indice,n)
    return ordenada_nova