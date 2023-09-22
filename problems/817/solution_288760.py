def acima_da_media(lista):
    """coment"""
    list.sort(lista)
    media=sum(lista)/len(lista)
    if m in lista:
        list.remove(lista,m)
    ind=list.index(lista,m)
    lista[:ind+1]=[]
    return lista
    else:
        return lista