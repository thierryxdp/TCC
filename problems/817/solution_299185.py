def maiores(lista, n):
    lista.sort()
    listamaior = [x for x in lista if x > n]
    return listamaior

def acima_da_media(notas):
    media = sum(notas) / len(notas)
    return maiores(notas, media)