def repetidos(lista):
    """Dado uma lista com números, a função retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list->int"""
    contador=0
    indice=1
    while indice<len(lista):
        if lista[indice-1]==lista[indice]:
            contador=contador+1
            indice=indice+1
        else:    
            indice=indice+1
    return contador