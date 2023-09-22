def acima_da_media(lista):
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    x=list.index(lista,media)
    lista=lista[x:]
    del lista[0]
    list.remove(lista,media)
    return lista