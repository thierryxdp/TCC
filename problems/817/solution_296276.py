def acima_da_media(lista):
    n=sum(lista)/len(lista)
    if n in lista:
        list.append(lista, n)
        list.sort(lista)
        indice=list.index(lista, n) + 1
        lista1=lista[indice::]
        return lista1
    else:
        list.append(lista, n)
        list.sort(lista)
        indice=list.index(lista, n) + 1
        lista1=lista[indice::]
        list.remove(lista1, n)
        return lista1