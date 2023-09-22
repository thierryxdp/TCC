def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma//quantidade
    lista.sort()
    return lista[media+0.5:]