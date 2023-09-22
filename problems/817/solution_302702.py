def acima_da_media(lis):
    """A função receb uma lista, calculando a sua média e retornando uma lista com os valores acima da média em ordem crescente. """
    maiores_notas = list()
    media = sum(lis)/len(lis)
    for c in lis:
        if c > media:
            maiores_notas.append(c)
            maiores_notas.sort()
    return maiores_notas