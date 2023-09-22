def acima_da_media(lista):
    if media in lista:
        quantidade = len(lista)
        soma = sum(lista)
        media = soma//quantidade
        lista.sort()
        posicao = list.index(lista,media)
        return lista[posicao+1:]
    else:
        return lista