def maiores(lista, n):
    list.insert(lista,0, n)
    list.sort(lista)
    i=list.index(lista, n)
    return lista[i+1:]
def acima_da_media(notas):
    media=sum(notas)/len(notas)
    if media in notas:
        list.remove(notas, media)
    	return maiores(notas, media)
    elif media not in notas:
        return maiores(notas, media)
    elif len(notas)==1:
        return []