def acima_da_media(lista):
    """retorna uma lista com as notas que ficaram acima da média
    list->list"""
    list.sort(lista)
    a=list.index(lista,6)
    return lista[a:]