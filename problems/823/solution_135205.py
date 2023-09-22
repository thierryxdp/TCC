def faltante(lista_inteiros):
    indice = 1
    while indice<len(lista_inteiros):
        if lista_inteiros[indice]-(lista_inteiros[indice-1])==2:
            lista_nova = lista_inteiros[indice] + (lista_inteiros[indice]-1)
        indice = indice+1
    return list.sort(lista_nova)