def acima_da_media(lista):
    n=sum(lista)/len(lista)
    list.append(lista, n)
    list.sort(lista)
    indice=list.index(lista, n) + 1
    lista1=lista[indice::]
    list.remove(lista1,n)
    if n in lista:
        return lista1
    else:
        list.append(lista1, n)
        list.sort(lista1)
        return lista1