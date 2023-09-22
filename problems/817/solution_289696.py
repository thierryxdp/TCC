def acima_da_media(lista):
    lista=sorted(lista)
    lista=sum(lista)/len(lista)
    return lista[sum(lista)/len(lista):]