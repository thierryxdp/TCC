def acima_da_media(lista):
    lista=sorted(lista)
    lista=sum(lista)/len(lista)
    return int(lista)>sum(lista)/len(lista)