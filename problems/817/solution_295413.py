def acima_da_media(notas):
    import.math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    return notas[0:media]