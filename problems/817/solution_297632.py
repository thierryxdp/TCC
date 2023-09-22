def acima_da_media(lista):
    x=sum(lista)
    y=len(lista)
    n=x//y
    list.append(lista,n)
    list.sort(lista)
    A=list.index(lista,n)
    B=list.count(lista,n)
    return lista[A+B:]