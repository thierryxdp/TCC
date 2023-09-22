def acima_da_media (notas):
    media = sum(notas) / len(notas)
    list.append(notas, media)
    list.sort(notas)
    indice = list.index(notas, media)
    acima = notas[indice:]
    return acima