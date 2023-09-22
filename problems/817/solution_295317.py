def acima_da_media(lista):
    s=sum(lista)/len(lista)
    lista.append(s)
    lista.sort()
    x=lista.index(s)
    return lista[x:]