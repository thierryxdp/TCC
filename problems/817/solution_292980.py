def acima_da_media(notas):
    media = sum(notas)/4
    acima = [x for x in notas if x > media]
    return acima