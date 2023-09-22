def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    lista2=lista[a+1:]
    return lista2


def acima_da_media(lista):
    media=sum(lista)/len(lista)
    return(maiores(lista,media)