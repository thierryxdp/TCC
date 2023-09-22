def acima_da_media(lista):
    """retorna uma lista ordenada com as notas que ficaram acima da média, dada a lista com as notas.
    list->list"""
    soma=sum(lista)
    media=soma/len(lista)
    
    list.append(lista,media)
    list.sort(lista)
    n=list.index(lista,media)
    del lista[:n+1]