def acima_da_media(lista):
    l=len(lista)
    p=sum(lista)/l
    lista.insert(0,p)
    lista.sort()
    indice=lista.index(p)
    return lista[indice+1:]