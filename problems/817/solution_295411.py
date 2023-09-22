def acima_da_media(notas):
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = soma/quantidade
    return notas[0:media]