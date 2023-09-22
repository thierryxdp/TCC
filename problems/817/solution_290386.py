def acima_da_media(lista):
    """retorna uma lista com as notas que ficaram acima da média
    list->list"""
    a=sum(lista)
    b=len(lista)
    c=a//b
    list.sort(lista)
    d=list.index(lista,c)
    if list.count(lista,c)>=1:
        return lista[d+1:]
    else:
        list.append(lista,c)
        list.sort(lista)
        e=list.index(lista,c)
        return lista[e+1:]