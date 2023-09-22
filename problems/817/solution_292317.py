def acima_da_media(lista):
    a=sum(lista)/len(lista)
    list.append(lista,a)
    list.sort(lista)
    b=list.index(lista,a)
    if lista[0]==4 or 8:
        return lista[b+1:]
    else:
        return lista[b+1:]