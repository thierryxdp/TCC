def acima_da_media(lista):
    media = sum(lista)/len(lista)
    if list.count(lista,media)>0:
        list.insert(lista,0,media)
        list.sort(lista)
        return lista[list.index(lista,media)+2:]
    else:
        list.insert(lista,0,media)
        list.sort(lista)
        return lista[list.index(lista,media)+1:]