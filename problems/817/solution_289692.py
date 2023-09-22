def acima_da_media(lista):
    lista=sorted(lista)
    lista=sum(lista)/len(lista)
    return len(lista)>sum(lista)/len(lista)