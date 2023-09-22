def acima_da_media(lista):
    """coment"""
    list.sort(lista)
    media=sum(lista)/len(lista)
    if media in lista:
        list.remove(lista,media)
        ind=list.index(lista,media)
        lista[:ind+1]=[]
        return lista
    else:
        return lista