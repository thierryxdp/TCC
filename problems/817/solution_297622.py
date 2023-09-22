def acima_da_media(lista):
    x=sum(lista)
    y=len(lista)
    list.sort(lista)
    return lista[x+y//2:]