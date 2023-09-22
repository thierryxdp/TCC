def acima_da_media(lista):
    aprovados = []
    media = sum(lista) / len(lista)
    for elemento in lista:
        if elemento > media:
            aprovados += [elemento]
    return aprovados