def maiores(lista,n):
    lista1=lista+[n]
    list.sort(lista1)
    lista2 = lista1[list.index(lista1,n) +1:]
    return lista2

def acima_da_media(notas):
    lista2=notas
    M=media
    M= sum(notas)/len(notas)
    list.sort
    return (lista2,M)