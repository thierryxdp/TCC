def acima_da_media(lis):
    maiores_numeros = list()
    for c in lis:
            maiores_numeros.append(c)
            list.sort(maiores_numeros)
    return maiores_numeros