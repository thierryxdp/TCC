def acima_da_media(lista):
    maiores_numeros = list()
    for c in lista:
        if c >= 5:
            maiores_numeros.append(c)
        elif c > 5:
            maiores_numeros.append(c)
    list.sort(maiores_numeros)
    return maiores_numeros