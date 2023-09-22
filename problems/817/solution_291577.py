def acima_da_media(lista):
    quantidade = len(lista)
    soma = sum(lista)
    media = soma//quantidade
    lista.sort()
        if media in lista:
        posicao = list.index(lista,media)
        return lista[posicao+1:]
    else:
        return lista