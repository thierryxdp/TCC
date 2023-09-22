def acima_da_media(lista):
    s=sum(lista)/len(lista)
    lista.append(s+0.1)
    lista.sort()
    x=lista.index(s+0.1)
    return lista[x+1:]