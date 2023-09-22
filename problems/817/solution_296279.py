def acima_da_media(lista):
    n=sum(lista)/len(lista)
    list.append(lista, n)
    list.sort(lista)
    indice=list.index(lista, n) + 1
    lista1=lista[indice::]
    if n in lista:
        return lista1
    else:
        list.remove(lista1, n)
        return lista1