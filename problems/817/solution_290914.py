def acima_da_media(notas):
    notas.sort()
    return [i for i in notas if i > 5]