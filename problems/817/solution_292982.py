def acima_da_media(notas):
    media = sum(notas)/len(notas)
    acima = [x for x in notas if x > media]
    return sorted(acima)