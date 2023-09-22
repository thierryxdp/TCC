def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = (soma/quantidade)
    a = list.index (notas, media)
    return notas[a:]