def acima_da_media(lista):
    lista=sorted(lista)
    x=sum(lista)/len(lista)
    lista=len(lista)>x
    return lista