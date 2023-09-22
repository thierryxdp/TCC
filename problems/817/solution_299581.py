def maiores(lis, n):
    maiores_numeros = list()
    for c in lis:
        if c >= n:
            maiores_numeros.append(c)
    return sorted(maiores_numeros)

def acima_da_media(lista,m):
    lista= sum(maiores(lista,m))//len(maiores(lista,m))
    return lista