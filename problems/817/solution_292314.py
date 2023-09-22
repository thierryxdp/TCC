def acima_da_media(lista):
    a=sum(lista)/len(lista)
    list.append(lista,a)
    list.sort(lista)
    b=list.index(lista,a)
    if a in lista:
        return lista[b+2:]
    else:
        return lista[b+1:]