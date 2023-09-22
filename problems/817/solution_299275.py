def acima_da_media(lista):
    
    media = sum(lista)//len(lista)
    lista.append(media)
    list.sort(lista)
    start = lista.index(media) + lista.count(media)
    return lista[start:]