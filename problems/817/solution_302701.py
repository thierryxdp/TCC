def acima_da_media(lis):
    maiores_notas = list()
    media = sum(lis)/len(lis)
    for c in lis:
        if c > media:
            maiores_notas.append(c)
            maiores_notas.sort()
    return maiores_notas