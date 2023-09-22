def acima_da_media(notas):
    m = sum(notas)/len(notas)
    lista = notas + [m]
    list.sort(lista)
    k = list.index(lista,m)
    acima = lista[k+1:]
    return acima