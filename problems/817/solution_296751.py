def acima_da_media(lis):
    y=(sum(lis)/len(lis))
    maiores_numeros = list()
    for c in lis:
        if c >= y:
            maiores_numeros.append(c)
            list.sort(maiores_numeros)
    return maiores_numeros