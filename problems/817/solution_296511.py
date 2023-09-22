def maiores(lista,n):
    lista1 = lista + [int(n)]
    list.sort(lista1)
    k = list.index(lista1,int(n))
    lista3 = lista1[k+1:]
    return lista3
def acima_da_media(notas):
    m = sum(notas)/len(notas)
    lista = notas + [m]
    list.sort(lista)
    k = list.index(lista,m)
    acima = lista1[k+1:]
    return acima