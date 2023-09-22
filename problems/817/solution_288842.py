def acima_da_media(lista):
    """Essa função retorna uma lista com as notas que ficaram acima
    da média. Como entrada temos uma lista de notas e como saida
    temos uma lista das notas que estão acima da média;
    list->list """
    list.sort(lista)
    soma=sum(lista)
    media=soma/len(lista)
    if media not in lista:
        list.append(lista,media)
        list.sort(lista)
        indice=list.index(lista,media)
        del lista[:indice+1]
        return lista 
    else:
        indice=list.index(lista,media)
        if lista[0]==indice:
            list.remove(lista,indice)
            return lista
        else:
            indice=list.index(lista,indice)
            del lista[:indice+1]
            return lista