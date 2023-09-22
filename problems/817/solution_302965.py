def acima_da_media(lista):
    """Esta função encontra a média das notas, e retorna os valores acima da média
    assinatura: list -> list
    """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    organizado = sorted(lista)
    im= organizado.index(media)
    acimamedia = organizado[im + 1:].copy()

    if media in acimamedia:
        del acimamedia[0]

    return acimamedia