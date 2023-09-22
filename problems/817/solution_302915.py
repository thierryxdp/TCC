def acima_da_media(lista):
    a=sum(lista)/len(lista)
    list.apend(lista,a)
    list.sort(lista)
    i=list.index(lista,a)
    return lista[1+1:]