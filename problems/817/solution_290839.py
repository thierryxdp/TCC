def acima_da_media(lista):
    media = floor(sum(lista) / len(lista))
    lista.sort()
    aprovados = lista[media+1:]
    return aprovados