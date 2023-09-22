def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
media=sum(lista)/len(lista)
g=media
if lista>media:
    return lista[g+1: ]
else:
    return [ ]