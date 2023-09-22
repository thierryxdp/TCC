def acima_da_media(lista):
    media =  sum(lista)/len(lista) 
    list.append(lista,media)
    list.sort(lista)
    lista = lista[lista.index(media)+1:]
    if media in lista:
        list.remove(lista,media)
        return lista
    else:
        return lista