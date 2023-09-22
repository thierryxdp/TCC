def acima_da_media(lista):
    media=sum(lista)/len(lista)
    list.sort(lista)
    lista2=lista[media:]
    return lista2