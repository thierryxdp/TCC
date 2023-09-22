def faltante(lista_inteiros):
    indice = 1
    lista_inteiros = []
    while indice<len(lista_inteiros):
        if lista_inteiros[indice]-(lista_inteiros[indice-1])==2:
            lista_inteiros[indice] = lista_inteiros[indice]-1
            return lista_inteiros[indice]
        indice = indice+1
    return lista_inteiros[indice]