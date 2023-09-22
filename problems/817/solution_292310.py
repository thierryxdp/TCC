def acima_da_media(lista):
    a=sum(lista)/len(lista)
    list.append(lista,a)
    list.sort(lista)
    b=list.index(lista,a)
    return lista[b+1:]