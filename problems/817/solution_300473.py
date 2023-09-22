def acima_da_media(l):
    ''
	list.sort(l)
    s=sum(l)
    m=(s)/len(l)
    lista= l + [m]
    p=lista.index(m)
    lista=lista[p:] 
    lista.pop(0)
    return lista