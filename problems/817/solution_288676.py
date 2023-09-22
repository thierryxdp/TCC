def acima_da_media(notas):
    media = sum(notas) / len(notas)
    a = []
    idx = 0
    tam = len(notas)
    while idx < tam:
        nota = notas[idx]
        if nota > media:
            list.append(a, nota)
        idx += 1
    list.sort(a)
    return a