def acima_da_media(lista):
    a=int(sum(lista)/len(lista))
    if a in lista:
        b=list.index(lista,a)
        list.sort(lista)
        list.sort(lista)
        return lista[b+1:]
    else:
        list.append(lista,a)
        list.sort(lista)
        return lista[b+1:]