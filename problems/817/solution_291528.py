def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = (soma-5)//quantidade
    lista.sort()
    return lista[media:]