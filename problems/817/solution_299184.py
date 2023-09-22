def acima_da_media(notas):
    notas = notas_copia
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.sort(notas)
    if n in notas_copia:
        return notas[list.index(notas, n)+1:]
    elif n not in notas_copia:
        return notas[list.index(notas, n):]