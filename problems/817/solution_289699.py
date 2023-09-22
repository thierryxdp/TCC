def acima_da_media(lista):
    lista=sorted(lista)
    x=sum(lista)/len(lista)
    return int(lista[x:])