def faltante(lista_inteiros):
    indice = 1
    if lista_inteiros[0] != 1:
        return 1
    while indice<len(lista_inteiros):
        if lista_inteiros[indice]-(lista_inteiros[indice-1])==2:
            faltante = lista_inteiros[indice]-1
        if lista_inteiros[indice]-(lista_inteiros[indice-1])!=2::
            faltante = lista_inteiros[-1]+1
        indice = indice+1
    return faltante