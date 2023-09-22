def acima_da _media(lista):
    """retorna uma lista ordenada com as notas que ficaram acima da media, dada como entrada uma lista com as notas doas alunos.
    list->list"""
    soma=sum(lista)
    media=soma/int(len(lista))
    
    list.append(lista,media)
    list.sort(lista)
    x=list.index(lista,media)
    del lista[:x+1]
    return lista