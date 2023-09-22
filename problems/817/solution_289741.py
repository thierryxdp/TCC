def acima_da_media(lista):
    lista=sorted(lista)
    x=sum(lista)/len(lista)
    if x not in lista:
        list.append(lista,x)
        y=list.index(lista,x)
        a=y+1
        return lista[y:]
    else:
        y=list.index(lista,x)
        a=x+1
        return lista[y:]