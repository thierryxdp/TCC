def acima_da_media(notas):
    maior_que = 4
    filtrados = [x for x in notas if x > maior_que]
    return sorted(filtrados)