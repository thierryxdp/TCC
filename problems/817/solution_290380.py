def acima_da_media(lista):
    """retorna uma lista com as notas que ficaram acima da média
    list->list"""
    list.sort(lista)
    a=list.index(lista,7)
    b=a+1
    return lista[b:]