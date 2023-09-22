def acima_da_media(lista):
    n=sum(lista)/len(lista)
    list.append(lista,n)
    lista=sorted(lista)
    x=list.index(lista,n)
    y=x+2
    return lista[y:]