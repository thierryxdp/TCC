def acima_da_media(lista):
    x=sum(lista)/len(lista)
    if x not in lista:
        list.append(lista,x)
        lista=sorted(lista)
        y=list.index(lista,x)
        a=y+1
        return lista[a:]
    else:
        y=list.index(lista,x)
        lista=sorted(lista)
        a=y+1
        return lista[a:]