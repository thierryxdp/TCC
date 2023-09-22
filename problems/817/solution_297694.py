def acima_da_media (lista):
    x=sum(lista,0)
    y=len(lista)
    n=(x/y)
    d=[n]
    list.extend(lista,d)
    list.sort(lista)
    nova=list.index(lista,n)
    new=lista[nova+1:]
    return new//1