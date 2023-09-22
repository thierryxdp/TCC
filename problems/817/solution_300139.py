def acima_da_media(lista):
    if sum(lista) <= 6:
        return []

    media_das_notas = sum(lista) / len(notas)
    
    maiores_numeros = list()
    for c in lista:
        if c >= media_das_notas:
            maiores_numeros.append(c)
        list.sort(maiores_numeros)
    return maiores_numeros