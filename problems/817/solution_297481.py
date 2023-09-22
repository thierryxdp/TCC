def maiores(lista, n):
    list.insert(lista,0, n)
    list.sort(lista)
    i=list.index(lista, n)
    return lista[i:]
def acima_da_media(notas):
    media=sum(notas)/len(notas)
    return maiores(notas, media)