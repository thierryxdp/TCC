def acima_da_media(lista):
    """Essa função retorna uma lista com as notas que ficaram acima
    da média. Como entrada temos uma lista de notas e como saida
    temos uma lista das notas que estão acima da média;
    list->list """
    list.sort(lista)
    soma=sum(lista)
    media=round(soma/len(lista))
    indice=list.index(lista,media+1)
    del lista[:indice]
    return lista