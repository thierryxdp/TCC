def acima_da_media(lista):
    n = (sum(lista))//(len(lista))
    list.append(lista, n)
    list.sort(lista)
    return lista[(list.index(lista, n)): ]