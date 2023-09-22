def acima_da_media(lista):
    ind=list.index(lista, n)+1
    n=sum(lista)/ind
    list.append(lista, n)
    list.sort(lista)
    indice=list.index(lista, n) + 1
    lista1=lista[indice::]
    return lista1