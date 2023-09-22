def acima_da_media(lista):
    a=sum(lista)/len(lista)
    if a in lista:
        list.sort(lista)
        b=list.index(lista,a)
        return lista[b+1:]
    else:
        list.append(lista,a)
        list.sort(lista)
        b=list.index(lista,a)
        return lista[b+1:]