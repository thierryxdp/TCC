def acima_da_media(lista):
    a=sum(lista)/len(lista)
    lista.append(a)
    list.sort(lista)
    return lista[lista.index(int.a)+1:]