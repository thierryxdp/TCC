def acima_da_media(lista):
    n=sum(lista)/range(lista)
    list.append(lista, n)
    list.sort(lista)
    indice=list.index(lista, n) + 1
    lista1=lista[indice::]
    return lista1