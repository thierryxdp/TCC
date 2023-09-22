def faltante(lista_inteiros):
    faltante = int(faltante)
    indice = 1
    lista_inteiros = list.sort(lista_inteiros)
    return lista_inteiros
    while indice<=len(lista_inteiros):
        if lista_inteiros[indice]-(lista_inteiros[indice-1])==2:
            faltante = lista_inteiros[indice]-1
        indice = indice+1
    return faltante