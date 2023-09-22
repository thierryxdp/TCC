def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma/quantidade
    lista.sort()
    v = lista.index(media)
    return lista[v:]