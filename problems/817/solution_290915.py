def acima_da_media(notas):
    notas.sort()
    media = sum(notas) / len(notas)
    return [i for i in notas if i > media]