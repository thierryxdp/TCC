def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma//quantidade
    lista.sort()
    posicao = list.index(lista,media)
    if posicao in lista:
        return lista[posicao+1:]
    if posicao not in lista:
        return lista[media:]