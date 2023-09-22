def acima_da_media(lista):
    """Retorna uma lista ordenada com as notas que ficaram acima da media.list-->list"""
    a=sum(lista)/len(lista)
    list.append(lista,a)
    list.sort(lista)
    b=list.index(lista,a)
    return lista[b+1::]