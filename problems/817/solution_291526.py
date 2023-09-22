def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = (soma-3)//quantidade
    lista.sort()
    return lista[media:]