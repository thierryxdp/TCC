def acima_da_media(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
            list.sort(maiores_numeros)
    return maiores_numeros