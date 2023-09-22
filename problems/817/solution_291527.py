def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = (soma-4)//quantidade
    lista.sort()
    return lista[media:]