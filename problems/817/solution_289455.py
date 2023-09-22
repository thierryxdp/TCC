def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    lista1=lista.index(media)
    return lista[lista1+lista.count(lista):]