def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return sorted(maiores_numeros)

def acima_da_media(lista):
    calculo= sum(lista)//len(lista)
    return calculo