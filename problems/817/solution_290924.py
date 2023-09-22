def acima_da_media(lista):
    a=sum(lista)/len(lista)
    lista.append(int(a))
    list.sort(lista)
    return lista[lista.index(a)+1:]