def acima_da_media(lista):
    n=sum(lista)//len(lista)
    list.append(lista,n)
    lista=sorted(lista)
    x=list.index(lista,n)
    y=x+1
    return lista[y:]