def acima_da_media(lista):
    if sum(lista) > acima_da_media:
        return lista
    
    maiores_numeros = list()
    for c in lista:
        if c >= 5:
            maiores_numeros.append(c)
        list.sort(maiores_numeros)
    return maiores_numeros